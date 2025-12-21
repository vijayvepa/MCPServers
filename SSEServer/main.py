import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

def print_env(key):
    print(f'{key}: {os.getenv(key)}')  # Print the value of LANGCHAIN_API_KEY

print_env("OPEN_AI_API_KEY")  # Print the value of OPENAI_API_KEY
print_env("LANGCHAIN_API_KEY")  # Print the value of OPENAI_API_KEY
print_env("LANGCHAIN_TRACING_V2")  # Print the value of OPENAI_API_KEY
print_env("LANGCHAIN_ENDPOINT")  # Print the value of OPENAI_API_KEY
print_env("LANGCHAIN_PROJECT")  # Print the value of OPENAI_API_KEY

import client
async def main():
    print("Hello from sseserver!")
    await client.client()


if __name__ == "__main__":
    asyncio.run(main())
