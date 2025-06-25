import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "server1": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.server1_mcp_tool]
        },
        "server2": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.server2_mcp_tool]
        }
    }
)