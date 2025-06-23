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
mcp_server_1_mcp_tool = tools_dir + "mcp_server_1_mcp.py"
############

# Agents settings
ORCHESTRATOR_PROMPT_PATH = "prompts/orchestrator_prompt.txt"
AGENT_ANALYTIC_PROMPT_PATH = "prompts/agent_analytic_prompt.txt"
AGENT_SENDER_PROMPT_PATH = "prompts/agent_sender_prompt.txt"
orchestrator_prompt = __read_doc(ORCHESTRATOR_PROMPT_PATH)
agent_analytic_prompt = __read_doc(AGENT_ANALYTIC_PROMPT_PATH)
agent_sender_prompt = __read_doc(AGENT_SENDER_PROMPT_PATH)

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