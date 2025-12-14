#!/usr/bin/env python3
"""
Script to disable all Cursor/VSCode extensions.
Works by modifying the settings.json file to disable all extensions.
"""

import json
import os
import sys
import subprocess
from pathlib import Path

def find_cursor_settings():
    """Find Cursor settings.json file locations."""
    settings_paths = []
    
    # Workspace settings
    workspace_settings = Path.cwd() / ".vscode" / "settings.json"
    if workspace_settings.exists():
        settings_paths.append(workspace_settings)
    
    # User settings (Windows)
    if sys.platform == "win32":
        user_settings = Path.home() / "AppData" / "Roaming" / "Cursor" / "User" / "settings.json"
        if user_settings.exists():
            settings_paths.append(user_settings)
    elif sys.platform == "darwin":  # macOS
        user_settings = Path.home() / "Library" / "Application Support" / "Cursor" / "User" / "settings.json"
        if user_settings.exists():
            settings_paths.append(user_settings)
    else:  # Linux
        user_settings = Path.home() / ".config" / "Cursor" / "User" / "settings.json"
        if user_settings.exists():
            settings_paths.append(user_settings)
    
    return settings_paths

def get_installed_extensions():
    """Get list of installed extensions using CLI commands."""
    extensions = []
    
    # Try cursor command
    for cmd in ["cursor", "code"]:
        try:
            result = subprocess.run(
                [cmd, "--list-extensions"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                extensions = [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]
                return extensions, cmd
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    return None, None

def disable_extensions_via_cli(extensions, cmd_name):
    """Disable extensions using CLI commands (batch mode to avoid opening windows)."""
    # Note: This method is deprecated in favor of settings.json modification
    # which doesn't open any windows. Kept for backward compatibility.
    disabled = []
    failed = []
    
    print(f"\nDisabling {len(extensions)} extensions using '{cmd_name}' command...")
    print("  (Note: Using settings.json method is recommended to avoid opening windows)")
    
    # Try to disable all at once by building a single command
    # However, VSCode/Cursor CLI doesn't support multiple extensions in one command
    # So we'll use settings.json method instead
    print("  Switching to settings.json method to avoid opening windows...")
    return disabled, failed

def disable_extensions_via_settings(settings_path, extensions=None):
    """Disable extensions by modifying settings.json."""
    try:
        # Read existing settings
        if settings_path.exists():
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)
        else:
            settings = {}
            settings_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Get extensions if not provided
        if extensions is None:
            extensions, cmd_name = get_installed_extensions()
            if not extensions:
                extensions = []
        
        # Add disabled extensions to settings
        if "extensions.disabled" not in settings:
            settings["extensions.disabled"] = []
        
        # Add all extensions to disabled list (avoid duplicates)
        disabled_list = set(settings.get("extensions.disabled", []))
        if extensions:
            disabled_list.update(extensions)
        settings["extensions.disabled"] = sorted(list(disabled_list))
        
        # Also set other extension-related settings
        settings["extensions.ignoreRecommendations"] = True
        settings["extensions.autoCheckUpdates"] = False
        settings["extensions.autoUpdate"] = False
        settings["extensions.showRecommendationsOnlyOnDemand"] = True
        
        # Write settings back
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)
        
        print(f"\n✓ Updated {settings_path}")
        if extensions:
            print(f"  Disabled {len(extensions)} extensions in settings")
        else:
            print(f"  Configured settings to prevent auto-enabling extensions")
        return True
            
    except Exception as e:
        print(f"\n✗ Error updating settings: {e}")
        return False

def main():
    """Main function to disable all extensions."""
    print("Cursor Extension Disabler")
    print("=" * 50)
    print("Using settings.json method (no windows will open)")
    print("=" * 50)
    
    # Get extensions list
    extensions, cmd_name = get_installed_extensions()
    
    if not extensions:
        print("\n⚠ Could not retrieve list of installed extensions.")
        print("  Attempting to use settings.json method anyway...")
        extensions = []
    
    if extensions:
        print(f"\nFound {len(extensions)} installed extensions")
    else:
        print("\n⚠ Could not list extensions via CLI.")
        print("  Will update settings.json to prevent auto-enabling.")
    
    response = input("\nDo you want to disable all extensions? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        return
    
    # Update settings.json files (primary method - no windows opened)
    print("\n" + "=" * 50)
    print("Updating settings.json files...")
    
    settings_paths = find_cursor_settings()
    
    if not settings_paths:
        # Create workspace settings if it doesn't exist
        workspace_settings = Path.cwd() / ".vscode" / "settings.json"
        settings_paths.append(workspace_settings)
    
    success_count = 0
    for settings_path in settings_paths:
        if disable_extensions_via_settings(settings_path, extensions):
            success_count += 1
    
    print("\n" + "=" * 50)
    if extensions:
        print(f"Summary:")
        print(f"  Extensions found: {len(extensions)}")
        print(f"  Settings files updated: {success_count}")
    else:
        print(f"Summary:")
        print(f"  Settings files updated: {success_count}")
    print("=" * 50)
    print("\nDone!")
    print("\nNote: Extensions are disabled in settings.json.")
    print("      You may need to restart Cursor for changes to take full effect.")

if __name__ == "__main__":
    main()

