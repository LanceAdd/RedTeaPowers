param(
    [Parameter(Mandatory = $true)]
    [string]$SessionDir
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-DescendantProcessIds {
    param([int]$RootPid)

    $seen = New-Object System.Collections.Generic.HashSet[int]
    $queue = New-Object System.Collections.Generic.Queue[int]
    $queue.Enqueue($RootPid)

    while ($queue.Count -gt 0) {
        $current = $queue.Dequeue()
        try {
            $children = Get-CimInstance Win32_Process -Filter "ParentProcessId = $current"
        } catch {
            $children = @()
        }

        foreach ($child in $children) {
            $childPid = [int]$child.ProcessId
            if ($seen.Add($childPid)) {
                $queue.Enqueue($childPid)
            }
        }
    }

    return @($seen)
}

$stateDir = Join-Path $SessionDir "state"
$pidFile = Join-Path $stateDir "server.pid"
$logFile = Join-Path $stateDir "server.log"

if (-not (Test-Path -LiteralPath $pidFile)) {
    Write-Output '{"status": "not_running"}'
    exit 0
}

$pidText = Get-Content -LiteralPath $pidFile -Raw -Encoding UTF8
if ($pidText) {
    $targetPid = [int]$pidText.Trim()
    $descendants = Get-DescendantProcessIds -RootPid $targetPid

    foreach ($childPid in ($descendants | Sort-Object -Descending)) {
        Stop-Process -Id $childPid -ErrorAction SilentlyContinue
    }

    Stop-Process -Id $targetPid -ErrorAction SilentlyContinue

    for ($i = 0; $i -lt 20; $i++) {
        Start-Sleep -Milliseconds 100
        $alive = @($descendants + $targetPid | Where-Object { Get-Process -Id $_ -ErrorAction SilentlyContinue })
        if ($alive.Count -eq 0) {
            break
        }
    }

    foreach ($childPid in ($descendants | Sort-Object -Descending)) {
        if (Get-Process -Id $childPid -ErrorAction SilentlyContinue) {
            Stop-Process -Id $childPid -Force -ErrorAction SilentlyContinue
        }
    }

    if (Get-Process -Id $targetPid -ErrorAction SilentlyContinue) {
        Stop-Process -Id $targetPid -Force -ErrorAction SilentlyContinue
        Start-Sleep -Milliseconds 100
    }

    $stillAlive = @($descendants + $targetPid | Where-Object { Get-Process -Id $_ -ErrorAction SilentlyContinue })
    if ($stillAlive.Count -gt 0) {
        Write-Output '{"status": "failed", "error": "process still running"}'
        exit 1
    }
}

Remove-Item -LiteralPath $pidFile -Force -ErrorAction SilentlyContinue
for ($i = 0; $i -lt 20; $i++) {
    try {
        Remove-Item -LiteralPath $logFile -Force -ErrorAction Stop
        break
    } catch {
        Start-Sleep -Milliseconds 100
    }
}

$resolvedSessionDir = [System.IO.Path]::GetFullPath($SessionDir)
$tempRoot = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
if ($resolvedSessionDir.StartsWith($tempRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    Remove-Item -LiteralPath $resolvedSessionDir -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Output '{"status": "stopped"}'
