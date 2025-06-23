import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "rag_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.rag_server_mcp_tool]
        }
    }
)