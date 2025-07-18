import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "confluence_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.confluence_server_mcp_tool]
        },
        "sberdru_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.sberdru_server_mcp_tool]
        },
        "sberusersoft_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.sberusersoft_server_mcp_tool]
        },
        "pulse_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.pulse_server_mcp_tool]
        }
    }
)