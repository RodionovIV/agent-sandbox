import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "RAGServer": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.RAGServer_mcp_tool]
        },
        "APIServer": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.APIServer_mcp_tool]
        },
        "WebSearchServer": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.WebSearchServer_mcp_tool]
        }
    }
)