import os
import sys

import requests
import logging
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP


load_dotenv()
_LOGGER = logging.getLogger(__name__)
mcp = FastMCP("sberusersoft_server", port=8000)


@mcp.tool()
def SberusersoftAPI():
    """API для установки ПО"""
    try:
        url = os.getenv("SBERUSERSOFTAPI")
        headers = {"Content-Type": "application/json"}
        data = json.dumps(data)
        response = requests.post(url, data, headers=headers)
        _LOGGER.info(f"Вызван post-tool для url {url}")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        e_str = f"Ошибка при отправлении запроса: {e}"
        _LOGGER.error(e_str)
        return e_str


if __name__ == "__main__":
    transport = sys.argv[1] if len(sys.argv) > 1 else "stdio"
    mcp.run(transport=transport)