# Cloud Authenticated MCP Server

- Get [Auth0](https://auth0.com/) account
- Get [CloudFlare](https://www.cloudflare.com/) account
- Install [Cloudflare Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/)
- Make sure git and node are available
- Clone [Cloudflare AI](https://github.com/cloudflare/ai) repo, go to demos folder
  - [Remote MCP Auth0](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-auth0) demo

## Arch Workflow 
- MCP Server is the OAuth Server for our MCP Client
- It issues access and refresh tokens
- MCP Server is the OAuth Client for Auth0 server
- It is OIDC client for the Auth0 server
- MCP Client thinks it is token provider

## Run Auth0 Demo
- cd todos-api
- npm install
- npm run dev
- It runs at port - [http://127.0.0.1:8789](http://127.0.0.1:8789)
- It will get error - requires auth0 domain, we need to setup auth0 project

## Auth 0 Setup
- Applications -> Apis -> Create API  
![img.png](img.png)

  - name: todos-api
  - identifier: urn:todos-api

![img_1.png](img_1.png)

- Quick Start - Nodejs - check code snippet
- [Original Instructions](https://github.com/cloudflare/ai/blob/main/demos/remote-mcp-auth0/todos-api/README.md)
### Settings
- Settings - allow offline access

![img_2.png](img_2.png)

![img_3.png](img_3.png)

### Permissions

Add below API permissions
- `read:todos`
-  `read:billing`


