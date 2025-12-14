@echo off
setlocal enabledelayedexpansion
REM Script to disable all Cursor/VSCode extensions on Windows

echo Cursor Extension Disabler
echo ================================================
echo.

REM Try to find cursor command
where cursor >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Found 'cursor' command
    set CMD_NAME=cursor
    goto :list_extensions
)

REM Try code command as fallback
where code >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Found 'code' command
    set CMD_NAME=code
    goto :list_extensions
)

echo ERROR: Could not find 'cursor' or 'code' command in PATH
echo Please ensure Cursor is installed and the CLI tools are available
pause
exit /b 1

:list_extensions
echo.
echo Listing installed extensions...
echo.

%CMD_NAME% --list-extensions > extensions_list.txt 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to list extensions
    pause
    exit /b 1
)

REM Count extensions
for /f %%i in ('type extensions_list.txt ^| find /c /v ""') do set EXT_COUNT=%%i
echo Found %EXT_COUNT% installed extensions
echo.

set /p CONFIRM="Do you want to disable all extensions? (y/n): "
if /i not "%CONFIRM%"=="y" (
    echo Cancelled.
    del extensions_list.txt
    pause
    exit /b 0
)

echo.
echo Disabling extensions via settings.json (no windows will open)...
echo.

REM Build JSON array of extensions
set JSON_EXTENSIONS=
set FIRST=1
for /f "delims=" %%e in (extensions_list.txt) do (
    if defined FIRST (
        set JSON_EXTENSIONS="%%e"
        set FIRST=
    ) else (
        set JSON_EXTENSIONS=!JSON_EXTENSIONS!, "%%e"
    )
)

REM Create/update workspace settings.json
if not exist ".vscode" mkdir .vscode

REM Check if settings.json exists and read it
set SETTINGS_FILE=.vscode\settings.json
if exist "%SETTINGS_FILE%" (
    REM Use PowerShell to update JSON (more reliable than batch)
    powershell -NoProfile -Command "$settings = Get-Content '%SETTINGS_FILE%' -Raw | ConvertFrom-Json; $extensions = Get-Content 'extensions_list.txt' | Where-Object { $_.Trim() -ne '' }; $settings | Add-Member -NotePropertyName 'extensions.disabled' -NotePropertyValue @($extensions) -Force; $settings.'extensions.ignoreRecommendations' = $true; $settings.'extensions.autoCheckUpdates' = $false; $settings.'extensions.autoUpdate' = $false; $settings.'extensions.showRecommendationsOnlyOnDemand' = $true; $settings | ConvertTo-Json -Depth 10 | Set-Content '%SETTINGS_FILE%'"
) else (
    REM Create new settings.json
    powershell -NoProfile -Command "$extensions = Get-Content 'extensions_list.txt' | Where-Object { $_.Trim() -ne '' }; $settings = @{ 'extensions.disabled' = @($extensions); 'extensions.ignoreRecommendations' = $true; 'extensions.autoCheckUpdates' = $false; 'extensions.autoUpdate' = $false; 'extensions.showRecommendationsOnlyOnDemand' = $true }; $settings | ConvertTo-Json -Depth 10 | Set-Content '%SETTINGS_FILE%'"
)

REM Count extensions
for /f %%i in ('type extensions_list.txt ^| find /c /v ""') do set EXT_COUNT=%%i

echo.
echo ================================================
echo Summary:
echo   Disabled: %EXT_COUNT% extensions via settings.json
echo ================================================
echo.
echo Note: Extensions are disabled in workspace settings.
echo       You may need to restart Cursor for changes to take full effect.

del extensions_list.txt
pause

