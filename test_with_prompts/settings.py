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
server1_mcp_tool = tools_dir + "server1_mcp.py"
############

# Agents settings
TEACHERAGENT_PROMPT_PATH = "prompts/TeacherAgent_prompt.txt"
ASSISTANTAGENT_PROMPT_PATH = "prompts/AssistantAgent_prompt.txt"
TUTORAGENT_PROMPT_PATH = "prompts/TutorAgent_prompt.txt"
TeacherAgent_prompt = __read_doc(TEACHERAGENT_PROMPT_PATH)
AssistantAgent_prompt = __read_doc(ASSISTANTAGENT_PROMPT_PATH)
TutorAgent_prompt = __read_doc(TUTORAGENT_PROMPT_PATH)

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