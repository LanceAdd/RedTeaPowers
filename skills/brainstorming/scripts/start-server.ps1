param(
    [string]$ProjectDir,
    [string]$HostName = "127.0.0.1",
    [string]$UrlHost,
    [switch]$Foreground,
    [switch]$Background
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-ParentPid {
    param([int]$ProcessId)

    try {
        $process = Get-CimInstance Win32_Process -Filter "ProcessId = $ProcessId"
        if ($null -eq $process) { return $null }
        return [int]$process.ParentProcessId
    } catch {
        return $null
    }
}

function Get-ChildProcessIds {
    param(
        [int]$ProcessId,
        [string]$Name
    )

    try {
        $children = Get-CimInstance Win32_Process -Filter "ParentProcessId = $ProcessId"
        if ($Name) {
            $children = $children | Where-Object { $_.Name -ieq $Name }
        }
        return @($children | Select-Object -ExpandProperty ProcessId)
    } catch {
        return @()
    }
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

if ([string]::IsNullOrWhiteSpace($UrlHost)) {
    if ($HostName -eq "127.0.0.1" -or $HostName -eq "localhost") {
        $UrlHost = "localhost"
    } else {
        $UrlHost = $HostName
    }
}

if (-not $Foreground -and -not $Background -and $env:CODEX_CI) {
    $Foreground = $true
}

$sessionId = "{0}-{1}" -f $PID, [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
if ($ProjectDir) {
    $resolvedProjectDir = (Resolve-Path -LiteralPath $ProjectDir).Path
    $sessionDir = Join-Path $resolvedProjectDir ".redteapowers\brainstorm\$sessionId"
} else {
    $sessionDir = Join-Path ([System.IO.Path]::GetTempPath()) "brainstorm-$sessionId"
}

$stateDir = Join-Path $sessionDir "state"
$contentDir = Join-Path $sessionDir "content"
$pidFile = Join-Path $stateDir "server.pid"
$logFile = Join-Path $stateDir "server.log"
$infoFile = Join-Path $stateDir "server-info"

[System.IO.Directory]::CreateDirectory($contentDir) | Out-Null
[System.IO.Directory]::CreateDirectory($stateDir) | Out-Null

if (Test-Path -LiteralPath $pidFile) {
    $oldPid = Get-Content -LiteralPath $pidFile -Raw -Encoding UTF8
    if ($oldPid) {
        Stop-Process -Id ([int]$oldPid.Trim()) -Force -ErrorAction SilentlyContinue
    }
    Remove-Item -LiteralPath $pidFile -Force -ErrorAction SilentlyContinue
}

$ownerPid = Get-ParentPid -ProcessId $PID
if ($ownerPid) {
    $grandParentPid = Get-ParentPid -ProcessId $ownerPid
    if ($grandParentPid -and $grandParentPid -ne 0) {
        $ownerPid = $grandParentPid
    }
}

if ($Foreground) {
    [System.IO.File]::WriteAllText($pidFile, "$PID", [System.Text.UTF8Encoding]::new($false))
    $env:BRAINSTORM_DIR = $sessionDir
    $env:BRAINSTORM_HOST = $HostName
    $env:BRAINSTORM_URL_HOST = $UrlHost
    if ($ownerPid) {
        $env:BRAINSTORM_OWNER_PID = "$ownerPid"
    }
    & node (Join-Path $scriptDir "server.cjs")
    exit $LASTEXITCODE
}

$nodeExe = (Get-Command node -ErrorAction Stop).Source
$startupScript = @"
`$env:BRAINSTORM_DIR = '$($sessionDir.Replace("'", "''"))'
`$env:BRAINSTORM_HOST = '$($HostName.Replace("'", "''"))'
`$env:BRAINSTORM_URL_HOST = '$($UrlHost.Replace("'", "''"))'
`$env:BRAINSTORM_OWNER_PID = '$ownerPid'
Set-Location '$($scriptDir.Replace("'", "''"))'
& '$($nodeExe.Replace("'", "''"))' 'server.cjs' 2>&1
"@

$encoded = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($startupScript))
for ($attempt = 1; $attempt -le 5; $attempt++) {
    Remove-Item -LiteralPath $logFile -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $infoFile -Force -ErrorAction SilentlyContinue

    $process = Start-Process -FilePath "powershell.exe" `
        -ArgumentList @("-NoProfile", "-EncodedCommand", $encoded) `
        -RedirectStandardOutput $logFile `
        -PassThru `
        -WindowStyle Hidden

    [System.IO.File]::WriteAllText($pidFile, "$($process.Id)", [System.Text.UTF8Encoding]::new($false))

    for ($i = 0; $i -lt 50; $i++) {
        Start-Sleep -Milliseconds 100

        if (Test-Path -LiteralPath $infoFile) {
            $serverPid = $null
            for ($k = 0; $k -lt 20; $k++) {
                $nodeChildren = Get-ChildProcessIds -ProcessId $process.Id -Name "node.exe"
                if ($nodeChildren.Count -gt 0) {
                    $serverPid = [int]$nodeChildren[0]
                    break
                }
                Start-Sleep -Milliseconds 100
            }

            if ($serverPid) {
                [System.IO.File]::WriteAllText($pidFile, "$serverPid", [System.Text.UTF8Encoding]::new($false))
            }

            $alive = $true
            for ($j = 0; $j -lt 20; $j++) {
                Start-Sleep -Milliseconds 100
                $trackedPid = if ($serverPid) { $serverPid } else { $process.Id }
                if (-not (Get-Process -Id $trackedPid -ErrorAction SilentlyContinue)) {
                    $alive = $false
                    break
                }
            }
            if (-not $alive) {
                Write-Output '{"error": "Server started but was killed. Retry with scripts/start-server.ps1 -Foreground in a persistent PowerShell session."}'
                exit 1
            }

            $line = Get-Content -LiteralPath $infoFile -Raw -Encoding UTF8
            Write-Output $line.Trim()
            exit 0
        }

        if ($process.HasExited) {
            break
        }
    }

    if (-not $process.HasExited) {
        Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
    }
}

Remove-Item -LiteralPath $pidFile -Force -ErrorAction SilentlyContinue
$errorText = if (Test-Path -LiteralPath $logFile) {
    (Get-Content -LiteralPath $logFile -Raw -Encoding UTF8 -ErrorAction SilentlyContinue).Trim()
} else {
    ""
}
if ([string]::IsNullOrWhiteSpace($errorText)) {
    Write-Output '{"error": "Server failed to start within 5 seconds"}'
} else {
    Write-Output ('{"error": "Server failed to start after retries. See server.log for details."}')
}
exit 1
