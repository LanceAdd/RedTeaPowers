param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ForwardArgs = @()
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "init_doc_structure.py"
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

$resolvedProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
$python = Get-PythonCommand

if ($null -eq $python) {
    throw "Python runtime not detected. Install Python or run the initializer through another wrapper."
}

$commandArgs = @()
$commandArgs += $python.Args
$commandArgs += $pythonScript
$commandArgs += $resolvedProjectRoot
$commandArgs += $ForwardArgs

& $python.Exe @commandArgs
exit $LASTEXITCODE
