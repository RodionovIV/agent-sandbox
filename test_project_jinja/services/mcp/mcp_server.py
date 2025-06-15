import json
import os
import sys

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp_server_1", port=8000)


@mcp.tool()
def test_get():
    """TEST GET MCP TOOL"""
    try:
        url = os.getenv("TEST_GET")
        response = requests.get(url)
        print(f"Вызван get-tool для url {url}")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        e_str = f"Ошибка при отправлении запроса: {e}"
        print(e_str)
        return e_str



@mcp.tool()
def test_post(data):
    """TEST POST MCP TOOL"""
    try:
        url = os.getenv("TEST_POST")
        headers = {"Content-Type": "application/json"}
        data = json.dumps(data)
        response = requests.post(url, data, headers=headers)
        print(f"Вызван post-tool для url {url}")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        e_str = f"Ошибка при отправлении запроса: {e}"
        print(e_str)
        return e_str


if __name__ == "__main__":
    transport = sys.argv[1] if len(sys.argv) > 1 else "stdio"
    mcp.run(transport=transport)