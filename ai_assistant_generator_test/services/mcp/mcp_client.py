import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "Server1": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.Server1_mcp_tool]
        },
        "Server2": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.Server2_mcp_tool]
        }
    }
)