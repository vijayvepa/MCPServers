"""Simple MCP server with terminal tool."""
import subprocess
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Terminal Server")


@mcp.resource("file://readme")
def readme_resource() -> str:
    """
    Provides the contents of the README.md file.
    
    Returns:
        The contents of README.md as a string
    """
    readme_path = Path(__file__).parent / "README.md"
    
    if not readme_path.exists():
        return "README.md file not found"
    
    try:
        return readme_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading README.md: {str(e)}"


@mcp.tool()
def terminal_tool(command: str) -> dict[str, Any]:
    """
    Execute a terminal command and return the output.
    
    Args:
        command: The terminal command to execute
        
    Returns:
        A dictionary containing the command output, exit code, and any errors
    """
    if not command or not command.strip():
        return {
            "output": "",
            "exit_code": 1,
            "error": "Command cannot be empty"
        }
    
    try:
        # Execute the command using subprocess
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout for safety
        )
        
        return {
            "output": result.stdout,
            "error_output": result.stderr,
            "exit_code": result.returncode,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "exit_code": -1,
            "error": "Command execution timed out after 30 seconds"
        }
    except Exception as e:
        return {
            "output": "",
            "exit_code": -1,
            "error": f"Error executing command: {str(e)}"
        }


def main() -> None:
    """Run the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
