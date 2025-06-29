import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "translation_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.translation_server_mcp_tool]
        },
        "speech_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.speech_server_mcp_tool]
        }
    }
)