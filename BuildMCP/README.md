# Goal 2: Build an MCP Sever


## Resources
- [Github Repo](https://github.com/emarco177/mcp-crash-course)
- [Install UV](https://docs.astral.sh/uv/getting-started/installation/#pypi)
  - pip install in git bash
     ```shell
        pip install uv
    ```


## Overview
- Initialize project with UV
- Create venv with UV
- Install dependencies MCP[CLI]
- Index official documentation with Cursor
- Update project with cursor rules

### Initialize Project with UV
```shell
uv init shell-server
cd mcp-server
uv venv
source .venv/Scripts/activate
uv add "mcp[cli]"
```

## Add docs to Cursor

- Go to cursor settings and add the MCP docs to index
- https://modelcontextprotocol.io 
- https://github.com/modelcontextprotocol/python-sdk

![img.png](img.png)

## Add rules to Cursor
- Go to [cursor.directory](https://cursor.directory)
- Search for python, fastapi, scalable API development
- Add to .cursor/python.mdc
- Run below prompt

```prompt
I want you to implement me a simple MCP server from @MCP Docs  Use python SDK @MCP Python SDK  and the server should expose one tool which is called terminal tool which will allow user to run terminal commands, make it simple.
```

![img_1.png](img_1.png)

## Run MCP Server

```shell
uv run server.py
```

## Add to Claude

"C:\Users\vijay\AppData\Roaming\Claude\claude_desktop_config.json"

```json
{
	"mcpServers": {
		"shell-server": {
			"command": "C:\\Users\\vijay\\AppData\\Roaming\\Python\\Python313\\Scripts\\uv",
			"args": [
				"--directory",
				"I:\\Code\\Udemy\\MCPServers\\shellserver",
				"run",
				"server.py"
			]
		}
	}
}
```

![img_3.png](img_3.png)

![img_2.png](img_2.png)

## Test in Claude

```prompt
Show me all the files in my desktop folder
```
![img_4.png](img_4.png)

![img_5.png](img_5.png)

## Expose a Resource in MCP Server

```prompt
Expose @README.md as a resource in my MCP Server using @MCP Docs and @MCP Python SDK 
```

![img_7.png](img_7.png)

### Testing 

![img_6.png](img_6.png)

![img_8.png](img_8.png)