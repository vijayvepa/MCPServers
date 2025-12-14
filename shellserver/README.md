# Shell Server

Add your description here

## Disabling Cursor Extensions

This project includes scripts to disable all Cursor/VSCode extensions. Extensions are disabled by default through workspace settings, and you can use the provided scripts to disable all currently installed extensions.

### Workspace Settings

The `.vscode/settings.json` file is configured to:
- Ignore extension recommendations
- Disable automatic extension updates
- Prevent extensions from auto-enabling

### Scripts to Disable All Extensions

Three scripts are provided to disable all installed extensions:

#### 1. Python Script (Cross-platform)
```bash
python disable_extensions.py
```

This script:
- Lists all installed extensions
- Disables them via CLI commands
- Updates settings.json files to ensure extensions stay disabled

#### 2. PowerShell Script (Windows)
```powershell
.\disable_extensions.ps1
```

#### 3. Batch Script (Windows)
```cmd
disable_extensions.bat
```

### Prerequisites

For the scripts to work, you need to have Cursor CLI tools installed:
- Open Cursor
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
- Run: "Shell Command: Install 'cursor' command in PATH"

### Manual Method

If the scripts don't work, you can manually disable extensions:

1. Open Extensions view (`Ctrl+Shift+X`)
2. Click the gear icon (⚙️) next to each extension
3. Select "Disable" for each extension

Or use Command Palette (`Ctrl+Shift+P`):
- Run "Extensions: Disable All Installed Extensions"

### Re-enabling Extensions

To re-enable specific extensions:
1. Open Extensions view (`Ctrl+Shift+X`)
2. Find the extension you want
3. Click "Enable"

Or remove the extension ID from the `extensions.disabled` array in `.vscode/settings.json`.






