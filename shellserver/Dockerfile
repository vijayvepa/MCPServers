FROM python:3.13-slim AS builder
# Add uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Preload lockfile/deps to leverage Docker layer caching
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-editable

# Bring in the rest of the source and finish syncing
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

# Runtime image
FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app

# Copy the synced environment and app code
COPY --from=builder /app /app

# Use the project virtualenv for all commands
ENV PATH="/app/.venv/bin:${PATH}"

# Default command matches local usage: uv run server.py
CMD ["uv", "run", "server.py"]
