import json
import os
import sys

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("database_server", port=8000)


@mcp.tool()
def DatabaseAPI():
    """API для взаимодействия с базой данных"""
    try:
        url = os.getenv("DATABASEAPI")
        response = requests.get(url)
        print(f"Вызван get-tool для url {url}")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        e_str = f"Ошибка при отправлении запроса: {e}"
        print(e_str)
        return e_str


if __name__ == "__main__":
    transport = sys.argv[1] if len(sys.argv) > 1 else "stdio"
    mcp.run(transport=transport)