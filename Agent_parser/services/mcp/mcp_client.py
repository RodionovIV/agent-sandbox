import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "web_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.web_server_mcp_tool]
        },
        "rag_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.rag_server_mcp_tool]
        }
    }
)