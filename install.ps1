# Run with the normal PowerShell policy. This script does not bypass it.
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$WorkbenchArguments)
$ErrorActionPreference = 'Stop'
$WorkbenchRoot = $PSScriptRoot
foreach ($Candidate in @('python', 'python3', 'py')) {
    if (Get-Command $Candidate -ErrorAction SilentlyContinue) {
        & $Candidate -c 'import sys,venv; sys.exit(sys.version_info < (3,11))' 2>$null
        if ($LASTEXITCODE -eq 0) {
            & $Candidate (Join-Path $WorkbenchRoot 'workbench.py') setup @WorkbenchArguments
            exit $LASTEXITCODE
        }
    }
}
if ($WorkbenchArguments -contains '--offline') {
    throw 'Offline mode requires existing Python 3.11+; no download was started.'
}
Write-Host 'Preparing local Python through pinned Astral uv. No global environment or policy changes.'
$Workspace = Join-Path ([Environment]::GetFolderPath('UserProfile')) 'ResearchWorkbench'
for ($Index = 0; $Index -lt $WorkbenchArguments.Count; $Index++) {
    if ($WorkbenchArguments[$Index] -eq '--workspace') {
        $Index++
        if ($Index -ge $WorkbenchArguments.Count) { throw 'A workspace path is required.' }
        $Workspace = $WorkbenchArguments[$Index]
    } elseif ($WorkbenchArguments[$Index].StartsWith('--workspace=')) {
        $Workspace = $WorkbenchArguments[$Index].Substring(12)
    }
}
if ([string]::IsNullOrWhiteSpace($Workspace)) { throw 'A workspace path is required.' }
if ($Workspace.StartsWith('~/') -or $Workspace.StartsWith('~\')) {
    $Workspace = Join-Path ([Environment]::GetFolderPath('UserProfile')) $Workspace.Substring(2)
}
$Workspace = [IO.Path]::GetFullPath($Workspace)
$Separator = [IO.Path]::DirectorySeparatorChar
if ($Workspace -eq [IO.Path]::GetPathRoot($Workspace) -or $Workspace -eq [Environment]::GetFolderPath('UserProfile') -or ($WorkbenchRoot + $Separator).StartsWith($Workspace.TrimEnd($Separator) + $Separator, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Choose a dedicated workspace outside the installer source.'
}
$Control = Join-Path $Workspace '.workbench'
$Bootstrap = Join-Path $Control 'bootstrap'
foreach ($Path in @($Bootstrap, (Join-Path $Bootstrap 'uv'), (Join-Path $Bootstrap 'python'), (Join-Path $Bootstrap 'bin'), (Join-Path $Bootstrap 'cache'))) {
    $CheckPath = $Path
    while ($CheckPath) {
        if ((Test-Path -LiteralPath $CheckPath) -and ((Get-Item -Force -LiteralPath $CheckPath).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw 'Preserved a link or reparse point at the runtime destination.'
        }
        $CheckPath = [IO.Path]::GetDirectoryName($CheckPath)
    }
}
New-Item -ItemType Directory -Force -Path $Bootstrap | Out-Null
$SavedEnvironment = @{}
foreach ($Name in @('UV_UNMANAGED_INSTALL','UV_PYTHON_INSTALL_DIR','UV_PYTHON_BIN_DIR','UV_CACHE_DIR')) {
    $SavedEnvironment[$Name] = [Environment]::GetEnvironmentVariable($Name, 'Process')
}
try {
    $env:UV_UNMANAGED_INSTALL = Join-Path $Bootstrap 'uv'
    $env:UV_PYTHON_INSTALL_DIR = Join-Path $Bootstrap 'python'
    $env:UV_PYTHON_BIN_DIR = Join-Path $Bootstrap 'bin'
    $env:UV_CACHE_DIR = Join-Path $Bootstrap 'cache'
    $Uv = Join-Path $env:UV_UNMANAGED_INSTALL 'uv.exe'
    if (-not (Test-Path -LiteralPath $Uv)) {
        $Installer = Join-Path $Bootstrap ('uv-installer-' + [Guid]::NewGuid().ToString() + '.ps1')
        Invoke-WebRequest -Uri 'https://astral.sh/uv/0.12.22/install.ps1' -OutFile $Installer -UseBasicParsing
        if ((Get-FileHash -Algorithm SHA256 -LiteralPath $Installer).Hash.ToLowerInvariant() -ne '68e1f80e025c21e418f82c817de9bcbf96ce7fed36cbd7c40985a0b3c0055dea') {
            throw 'uv installer checksum mismatch; no downloaded code was executed.'
        }
        & $Installer
        if (-not (Test-Path -LiteralPath $Uv)) { throw 'uv installation did not produce the expected executable.' }
    }
    & $Uv run --no-project --python 3.12 python (Join-Path $WorkbenchRoot 'workbench.py') setup @WorkbenchArguments
    $WorkbenchExit = $LASTEXITCODE
} finally {
    foreach ($Name in $SavedEnvironment.Keys) {
        [Environment]::SetEnvironmentVariable($Name, $SavedEnvironment[$Name], 'Process')
    }
}
exit $WorkbenchExit
