import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "rag_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.rag_server_mcp_tool]
        },
        "web_search_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.web_search_server_mcp_tool]
        },
        "api_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.api_server_mcp_tool]
        }
    }
)