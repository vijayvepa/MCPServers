# Cloud Authenticated MCP Server

- Get [Auth0](https://auth0.com/) account
- Get [CloudFlare](https://www.cloudflare.com/) account
- Install [Cloudflare Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/)
- Make sure git and node are available
- Clone [Cloudflare AI](https://github.com/cloudflare/ai) repo, go to demos folder
  - [Remote MCP Auth0](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-auth0) demo

## Workflow 
- MCP Server is the OAuth Server for our MCP Client
- It issues access and refresh tokens
- MCP Server is the OAuth Client for Auth0 server
- It is OIDC client for the Auth0 server
- MCP Client thinks it is token provider