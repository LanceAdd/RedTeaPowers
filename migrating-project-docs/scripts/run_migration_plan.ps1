param(
    [Parameter(Mandatory = $true)]
    [string]$SourceRoot,
    [string]$Output,
    [string]$Title = "Legacy Documentation Migration Plan",
    [switch]$ForceFallback
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillDir = Split-Path -Parent $scriptDir
$pythonScript = Join-Path $scriptDir "generate_migration_plan.py"
$templatePath = Join-Path $skillDir "references\\003-manual-migration-plan-template.md"

function Get-PythonCommand {
    $candidates = @(
        @{ Exe = "python"; Args = @() },
        @{ Exe = "python3"; Args = @() },
        @{ Exe = "py"; Args = @("-3") }
    )

    foreach ($candidate in $candidates) {
        try {
            & $candidate.Exe @($candidate.Args + @("--version")) *> $null
            if ($LASTEXITCODE -eq 0) {
                return $candidate
            }
        } catch {
        }
    }

    return $null
}

function New-ManualFallbackContent {
    param(
        [string]$TemplateText,
        [string]$ResolvedSourceRoot,
        [string]$DocTitle
    )

    $generatedAt = [DateTime]::UtcNow.ToString("yyyy-MM-dd HH:mm 'UTC'")
    return $TemplateText.Replace("{{TITLE}}", $DocTitle).Replace("{{SOURCE_ROOT}}", $ResolvedSourceRoot).Replace("{{GENERATED_AT}}", $generatedAt)
}

$resolvedSourceRoot = (Resolve-Path -LiteralPath $SourceRoot).Path
$python = if ($ForceFallback) { $null } else { Get-PythonCommand }

if ($null -ne $python) {
    $arguments = @()
    $arguments += $python.Args
    $arguments += $pythonScript
    $arguments += $resolvedSourceRoot
    if ($Output) {
        $arguments += "--output"
        $arguments += $Output
    }
    if ($Title) {
        $arguments += "--title"
        $arguments += $Title
    }

    & $python.Exe @arguments
    exit $LASTEXITCODE
}

$templateText = Get-Content -Raw -LiteralPath $templatePath -Encoding UTF8
$content = New-ManualFallbackContent -TemplateText $templateText -ResolvedSourceRoot $resolvedSourceRoot -DocTitle $Title

Write-Warning "Python runtime not detected. Falling back to the manual migration plan template."

if ($Output) {
    $outputPath = [System.IO.Path]::GetFullPath($Output)
    $outputDir = Split-Path -Parent $outputPath
    if ($outputDir) {
        [System.IO.Directory]::CreateDirectory($outputDir) | Out-Null
    }
    [System.IO.File]::WriteAllText($outputPath, $content, [System.Text.UTF8Encoding]::new($false))
    Write-Host "Wrote manual fallback plan to $outputPath"
} else {
    Write-Output $content
}
