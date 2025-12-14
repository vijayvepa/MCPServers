# Script to disable all Cursor/VSCode extensions on Windows (PowerShell)

Write-Host "Cursor Extension Disabler" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Try to find cursor command
$cmdName = $null

if (Get-Command cursor -ErrorAction SilentlyContinue) {
    $cmdName = "cursor"
    Write-Host "Found 'cursor' command" -ForegroundColor Green
} elseif (Get-Command code -ErrorAction SilentlyContinue) {
    $cmdName = "code"
    Write-Host "Found 'code' command" -ForegroundColor Yellow
} else {
    Write-Host "ERROR: Could not find 'cursor' or 'code' command in PATH" -ForegroundColor Red
    Write-Host "Please ensure Cursor is installed and the CLI tools are available" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# List extensions
Write-Host ""
Write-Host "Listing installed extensions..." -ForegroundColor Cyan
Write-Host ""

$extensions = & $cmdName --list-extensions 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to list extensions" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

$extensionList = $extensions | Where-Object { $_.Trim() -ne "" }
$extCount = ($extensionList | Measure-Object).Count

Write-Host "Found $extCount installed extensions" -ForegroundColor Green
Write-Host ""

$confirm = Read-Host "Do you want to disable all extensions? (y/n)"
if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "Cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Disabling extensions via settings.json (no windows will open)..." -ForegroundColor Cyan
Write-Host ""

# Get workspace settings path
$workspaceSettings = Join-Path $PWD ".vscode\settings.json"
$workspaceDir = Split-Path $workspaceSettings -Parent

# Create .vscode directory if it doesn't exist
if (-not (Test-Path $workspaceDir)) {
    New-Item -ItemType Directory -Path $workspaceDir | Out-Null
}

# Read or create settings
if (Test-Path $workspaceSettings) {
    try {
        $settings = Get-Content $workspaceSettings -Raw | ConvertFrom-Json
    } catch {
        $settings = @{}
    }
} else {
    $settings = @{}
}

# Add all extensions to disabled list
$settings | Add-Member -NotePropertyName "extensions.disabled" -NotePropertyValue $extensionList -Force

# Set other extension-related settings
$settings | Add-Member -NotePropertyName "extensions.ignoreRecommendations" -NotePropertyValue $true -Force
$settings | Add-Member -NotePropertyName "extensions.autoCheckUpdates" -NotePropertyValue $false -Force
$settings | Add-Member -NotePropertyName "extensions.autoUpdate" -NotePropertyValue $false -Force
$settings | Add-Member -NotePropertyName "extensions.showRecommendationsOnlyOnDemand" -NotePropertyValue $true -Force

# Write settings back
$settings | ConvertTo-Json -Depth 10 | Set-Content $workspaceSettings -Encoding UTF8

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Disabled: $extCount extensions via settings.json" -ForegroundColor Green
Write-Host "  Settings file: $workspaceSettings" -ForegroundColor Gray
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Note: Extensions are disabled in workspace settings." -ForegroundColor Yellow
Write-Host "      You may need to restart Cursor for changes to take full effect." -ForegroundColor Yellow
Write-Host ""

Read-Host "Press Enter to exit"

