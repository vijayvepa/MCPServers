#!/usr/bin/env bash
set -euo pipefail

# Build the Docker image for the MCP shell server.
docker build -t mcp-shellserver:latest .
