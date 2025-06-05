from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from agents.agent import BaseAgent


class OrchestratorAgent(BaseAgent):
    def __init__(self, tools: list[BaseTool], llm: ChatOpenAI):
        super().__init__(tools, llm)

    def run(self, input: str) -> str:
        # ÐÐ¾Ð¾ÑÐ´Ð¸Ð½Ð°ÑÐ¸Ñ ÑÐ°Ð±Ð¾ÑÑ Ð²ÑÐµÑ Ð°Ð³ÐµÐ½ÑÐ¾Ð²
        return super().run(input)
