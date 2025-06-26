import os
from functools import lru_cache

from langchain_gigachat.chat_models import GigaChat

# Application settings
LOG_FILE = "app.log"

@lru_cache()
def __read_doc(path):
    with open(path, mode="r") as f:
        return f.read()

base_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = base_dir + "/services/"

# MCP Tools
database_server_mcp_tool = tools_dir + "database_server_mcp.py"
grafana_server_mcp_tool = tools_dir + "grafana_server_mcp.py"
############

# Agents settings
DATAANALYZER_PROMPT_PATH = "prompts/DataAnalyzer_prompt.txt"
DASHBOARDSENDER_PROMPT_PATH = "prompts/DashboardSender_prompt.txt"
DataAnalyzer_prompt = __read_doc(DATAANALYZER_PROMPT_PATH)
DashboardSender_prompt = __read_doc(DASHBOARDSENDER_PROMPT_PATH)

# Model settings
llm = GigaChat(
    model="GigaChat-2-Max",
    verify_ssl_certs=False,
    profanity_check=False,
    streaming=False,
    max_tokens=8192,
    temperature=0.3,
    repetition_penalty=1.01,
    timeout=180
)