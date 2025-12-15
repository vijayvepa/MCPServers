#!/usr/bin/env bash
set -euo pipefail

# Run the MCP shell server container using stdio transport.
docker run --rm -it mcp-shellserver:latest 