# Udemy Course - MCP Servers

## Goal 1: Leverage Existing MCP Server

### Resources
- [modelcontextprotocol/quickstart-resouces](https://github.com/modelcontextprotocol/quickstart-resources)
- [Cursor MCP](https://docs.cursor.com/context/model-context-protocol)
- [MCP.io Docs](https://modelcontextprotocol.io/docs/develop/build-server)

### Steps
- Cloned above repo
- Using weather-server-typescripts

```sh
cd quickstart-resources/weather-server-typescript
npm install
npm run build
```

- Add MCP Server in Settings

```json
{
  "mcpServers": {
		"weather": {
			"command": "node",
			"args": [
				"I:\\Code\\Udemy\\MCPServers\\quickstart-resources\\weather-server-typescript\\build\\index.js"
			]
		}
	}
}
```

![img.png](images/img.png)

- Test MCP Server

```prompt
what is the weather in SFO right now?

```

![img_1.png](images/img_1.png)

```prompt
Any weather alerts in SFO?
```