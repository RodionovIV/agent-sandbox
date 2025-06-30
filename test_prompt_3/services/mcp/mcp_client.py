import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "translation_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.translation_server_mcp_tool]
        },
        "tutoring_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.tutoring_server_mcp_tool]
        }
    }
)