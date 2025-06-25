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
RAGServer_mcp_tool = tools_dir + "RAGServer_mcp.py"
APIServer_mcp_tool = tools_dir + "APIServer_mcp.py"
WebSearchServer_mcp_tool = tools_dir + "WebSearchServer_mcp.py"
############

# Agents settings
PARSERAGENT_PROMPT_PATH = "prompts/ParserAgent_prompt.txt"
FORWARDERAGENT_PROMPT_PATH = "prompts/ForwarderAgent_prompt.txt"
ParserAgent_prompt = __read_doc(PARSERAGENT_PROMPT_PATH)
ForwarderAgent_prompt = __read_doc(FORWARDERAGENT_PROMPT_PATH)

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