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
rag_server_mcp_tool = tools_dir + "rag_server_mcp.py"
api_server_mcp_tool = tools_dir + "api_server_mcp.py"
############

# Agents settings
ORCHESTRATOR_PROMPT_PATH = "prompts/orchestrator_prompt.txt"
TEACHERAGENT_PROMPT_PATH = "prompts/teacherAgent_prompt.txt"
TRANSLATORAGENT_PROMPT_PATH = "prompts/translatorAgent_prompt.txt"
TUTORAGENT_PROMPT_PATH = "prompts/tutorAgent_prompt.txt"
orchestrator_prompt = __read_doc(ORCHESTRATOR_PROMPT_PATH)
teacherAgent_prompt = __read_doc(TEACHERAGENT_PROMPT_PATH)
translatorAgent_prompt = __read_doc(TRANSLATORAGENT_PROMPT_PATH)
tutorAgent_prompt = __read_doc(TUTORAGENT_PROMPT_PATH)

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