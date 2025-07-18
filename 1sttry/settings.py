import os
from functools import lru_cache
from dotenv import load_dotenv

from langchain_gigachat.chat_models import GigaChat

load_dotenv()

# Application settings
LOG_FILE = "app.log"

@lru_cache()
def __read_doc(path):
    with open(path, mode="r") as f:
        return f.read()

base_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = base_dir + "/services/mcp/"

# MCP Tools
confluence_server_mcp_tool = tools_dir + "confluence_server_mcp.py"
sberdru_server_mcp_tool = tools_dir + "sberdru_server_mcp.py"
sberusersoft_server_mcp_tool = tools_dir + "sberusersoft_server_mcp.py"
pulse_server_mcp_tool = tools_dir + "pulse_server_mcp.py"
############

# Agents settings
PARSERAGENT_PROMPT_PATH = "prompts/ParserAgent_prompt.txt"
EXECUTORAGENT_PROMPT_PATH = "prompts/ExecutorAgent_prompt.txt"
ParserAgent_prompt = __read_doc(PARSERAGENT_PROMPT_PATH)
ExecutorAgent_prompt = __read_doc(EXECUTORAGENT_PROMPT_PATH)

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