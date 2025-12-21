import os

from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
#from langchain.agents import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

llm = ChatOpenAI()
stdio_server_params = StdioServerParameters(
    command='python',
    args=[os.path.abspath(os.path.join(os.path.dirname(__file__), 'servers', 'math_server.py'))],
)

async def client():
    # Connect with stdio transport
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print('Session initialized.')
            tools = await session.list_tools()
            print(f"List Tools: {tools}")
            mcp_tools = await load_mcp_tools(session)
            print(f"Load MCP Tools: , ${mcp_tools}")
            agent = create_react_agent(llm, mcp_tools)
            result = await agent.ainvoke({
                "messages": [HumanMessage(content="What is 12 multiplied by 7, and then add 10 to the result?")]
            })
            print("---")
            print(result)
            print("----")
            print(result['messages'][-1].content)