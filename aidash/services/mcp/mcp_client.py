import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "database_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.database_server_mcp_tool]
        },
        "grafana_server": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.grafana_server_mcp_tool]
        }
    }
)