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

## Online API Keys

- [LangChain Smith](https://smith.langchain.com/)
- [Open API](https://platform.openai.com/api-keys)

## Environment Variables

In your user directory .bashrc or .zshrc; on in windows env vars

```shell
export LANGCHAIN_API_KEY="your_langchain_smith_key"
export OPENAI_API_KEY="your_openai_key"
```

## Run Math Server

```shell
uv run servers/math_server.py
```

## Run Weather Server (Server Sent Events)

```shell
$ uv run servers/weather_server.py
```

```log
INFO:     Started server process [45948]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```