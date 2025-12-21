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

## Run Client

```shell
uv run main.py
```

Session initialized.
### Tools Output
- [Tool(name='add', title=None, description='Add two numbers', inputSchema=
```json
{
  "properties": {
    "a": {
      "title": "A",
      "type": "integer"
    },
    "b": {
      "title": "B",
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ],
  "title": "addArguments",
  "type": "object"
}
```
, outputSchema=
```json
{
  "properties": {
    "result": {
      "title": "Result",
      "type": "integer"
    }
  },
  "required": [
    "result"
  ],
  "title": "addOutput",
  "type": "object"
}
```
, icons=None, annotations=None, meta=None, execution=None), 


- Tool(name='multiply', title=None, description='Multiply two numbers', inputSchema=
```json
 {
  "properties": {
    "a": {
      "title": "A",
      "type": "integer"
    },
    "b": {
      "title": "B",
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ],
  "title": "multiplyArguments",
  "type": "object"
}
```
, outputSchema=

```json
{
  "properties": {
    "result": {
      "title": "Result",
      "type": "integer"
    }
  },
  "required": [
    "result"
  ],
  "title": "multiplyOutput",
  "type": "object"
}
```
, icons=None, annotations=None, meta=None, execution=None)]

### MCP Tools Output 
- [StructuredTool(name='add', description='Add two numbers', args_schema=
```json 
 {
  "properties": {
    "a": {
      "title": "A",
      "type": "integer"
    },
    "b": {
      "title": "B",
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ],
  "title": "addArguments",
  "type": "object"
}
```
- , response_format='content_and_artifact', coroutine=<function convert_mcp_tool_to_langchain_tool.<locals>.call_tool at 0x000001D59ED1D760>), 

- StructuredTool(name='multiply
', description='Multiply two numbers', args_schema=
```json
 {
  "properties": {
    "a": {
      "title": "A",
      "type": "integer"
    },
    "b": {
      "title": "B",
      "type": "integer"
    }
  },
  "required": [
    "a",
    "b"
  ],
  "title": "multiplyArguments",
  "type": "object"
}
```
, response_format='content_and_artifact', coroutine=<function convert_mcp_tool_to_langchain_tool.<locals>.call_tool at 0x000001D59ED79800>)]

### LLM Request/Response

```python
{'messages': [HumanMessage(content='What is 12 multiplied by 7, and then add 10 to the result?', additional_kwargs={}, response_metadata={}, id='1a256309-e3de-41cb-a58a-8ac80603176d'), AIMessage(content
='', additional_kwargs={'refusal': None}, response_metadata=
```
```json 
{
  "token_usage": {
    "completion_tokens": 49,
    "prompt_tokens": 85,
    "total_tokens": 134,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": 0
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "model_provider": "openai",
  "model_name": "gpt-3.5-turbo-0125",
  "system_fingerprint": null,
  "id": "chatcmpl-CpEgqF0mq6L0Gn4P67Bv8naLGm6JC",
  "service_tier": "default",
  "finish_reason": "tool_calls",
  "logprobs": null
} 
```
id="lc_run--019b414e-a1d4-7672-8c93-a7882d38e68f-0"}
tool_calls=
```json
[
  {
    "name": "multiply",
    "args": {
      "a": 12,
      "b": 7
    },
    "id": "call_PhqvXHtb148DCgcdrvRpabRF",
    "type": "tool_call"
  },
  {
    "name": "add",
    "args": {
      "a": 84,
      "b": 10
    },
    "id": "call_lEkhqaqyE9gzGGxIM2lxttdx",
    "type": "tool_call"
  }
]
```
, usage_metadata=
```json
{
  "input_tokens": 85,
  "output_tokens": 49,
  "total_tokens": 134,
  "input_token_details": {
    "audio": 0,
    "cache_read": 0
  },
  "output_token_details": {
    "audio": 0,
    "reasoning": 0
  }
}
```
, ToolMessage(content=[{'type': 'text', 'text': '84', 'id': 'lc_b18f589f-58d6-48b8-b589-fc7608e1d5a4'}], name='multiply', id='6a97a82b-8119-4a83-9ccd-6cd6b412007f', tool_call_id='
call_PhqvXHtb148DCgcdrvRpabRF', artifact={'structured_content': {'result': 84}}),

ToolMessage(content=[{'type': 'text', 'text': '94', 'id': 'lc_43785a91-1b89-4ad8-9d1f-b77e91e8d59a'}], name='add', id='1
ef6edcf-3e75-42e9-8461-0690d6c10126', tool_call_id='call_lEkhqaqyE9gzGGxIM2lxttdx', artifact={'structured_content': {'result': 94}}), 

### AI Message
AIMessage(content='12 multiplied by 7 is 84. When we add 10 to 84, the result is 94.', additional_kwargs={'refusal': None},

response_metadata=
```json
{
  "token_usage": {
    "completion_tokens": 25,
    "prompt_tokens": 150,
    "total_tokens": 175,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": 0
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "model_provider": "openai",
  "model_name": "gpt-3.5-turbo-0125",
  "system_fingerprint": null,
  "id": "chatcmpl-CpEgr0AB21QQjMHfhhg4AiSZzCZj6",
  "service_tier": "default",
  "finish_reason": "stop",
  "logprobs": null
}
```
, id="lc_run--019b414e-a9ad-7642-b691-afcdcaa10fc7-0", usage_metadata=
```json
{
  "input_tokens": 150,
  "output_tokens": 25,
  "total_tokens": 175,
  "input_token_details": {
    "audio": 0,
    "cache_read": 0
  },
  "output_token_details": {
    "audio": 0,
    "reasoning": 0
  }
}
```