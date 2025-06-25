import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "mcp_server_1": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.mcp_server_1_mcp_tool]
        },
        "mcp_server_2": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.mcp_server_2_mcp_tool]
        }
    }
)