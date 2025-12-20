# SSE Servers

# Installation and Setup

- Initialize uv

```shell
uv init
uv venv
source .venv/Scripts/activate 
```

- Install dependencies
```shell 
uv add langchain-mcp-adapters langchain-openai langgraph python-dotenv
```

- Test installation
```shell
uv run main.py
```