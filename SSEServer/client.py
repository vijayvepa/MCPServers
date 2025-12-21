import os

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

llm = ChatOpenAI()
stdio_server_params = StdioServerParameters(
    command='python',
    args=[f"I:\\Code\\Udemy\\MCPServers\\SSEServer\\servers\\math_server.py"],
)

async def client():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print('Session initialized.')
            tools = await session.list_tools()
            print(tools)
