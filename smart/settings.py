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
rag_server_mcp_tool = tools_dir + "rag_server_mcp.py"
api_server_mcp_tool = tools_dir + "api_server_mcp.py"
############

# Agents settings
VOICECOPILOT_PROMPT_PATH = "prompts/VOICECOPILOT_prompt.txt"
AGENTANALYZER_PROMPT_PATH = "prompts/AgentAnalyzer_prompt.txt"
AGENTCOORDINATOR_PROMPT_PATH = "prompts/AgentCoordinator_prompt.txt"
CHAT_PROMPT_PATH = "prompts/Chat_prompt.txt"
TICKETSYSTEM_PROMPT_PATH = "prompts/TicketSystem_prompt.txt"
VOICECOPILOT_prompt = __read_doc(VOICECOPILOT_PROMPT_PATH)
AgentAnalyzer_prompt = __read_doc(AGENTANALYZER_PROMPT_PATH)
AgentCoordinator_prompt = __read_doc(AGENTCOORDINATOR_PROMPT_PATH)
Chat_prompt = __read_doc(CHAT_PROMPT_PATH)
TicketSystem_prompt = __read_doc(TICKETSYSTEM_PROMPT_PATH)

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