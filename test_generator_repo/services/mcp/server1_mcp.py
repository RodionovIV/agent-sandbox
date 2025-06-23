import json
import os
import sys

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server1", port=8000)


@mcp.tool()
def RAG():
    """Инструмент для поиска и анализа данных."""
    try:
        url = os.getenv("RAG")
        response = requests.get(url)
        print(f"Вызван get-tool для url {url}")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        e_str = f"Ошибка при отправлении запроса: {e}"
        print(e_str)
        return e_str



@mcp.tool()
def Web Search():
    """Инструмент для веб-поиска."""
    try:
        url = os.getenv("WEB SEARCH")
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