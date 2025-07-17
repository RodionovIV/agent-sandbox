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
############

# Agents settings
GOALANALYZER_PROMPT_PATH = "prompts/GoalAnalyzer_prompt.txt"
GOALRESPONDER_PROMPT_PATH = "prompts/GoalResponder_prompt.txt"
GoalAnalyzer_prompt = __read_doc(GOALANALYZER_PROMPT_PATH)
GoalResponder_prompt = __read_doc(GOALRESPONDER_PROMPT_PATH)

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