from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from agents.agent import BaseAgent


class ValidatorAgent(BaseAgent):
    def __init__(self, tools: list[BaseTool], llm: ChatOpenAI):
        super().__init__(tools, llm)

    def run(self, input: str) -> str:
        # ÐÑÐ¾Ð²ÐµÑÐºÐ° ÐºÐ¾ÑÑÐµÐºÑÐ½Ð¾ÑÑÐ¸ ÑÐ°Ð±Ð¾ÑÑ Ð´ÑÑÐ³Ð¸Ñ Ð°Ð³ÐµÐ½ÑÐ¾Ð²
        return super().run(input)
