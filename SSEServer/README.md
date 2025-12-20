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

