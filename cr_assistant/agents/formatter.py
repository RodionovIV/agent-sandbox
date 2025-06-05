from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from agents.agent import BaseAgent


class FormatterAgent(BaseAgent):
    def __init__(self, tools: list[BaseTool], llm: ChatOpenAI):
        super().__init__(tools, llm)

    def run(self, input: str) -> str:
        # Ð¤Ð¾ÑÐ¼Ð¸ÑÐ¾Ð²Ð°Ð½Ð¸Ðµ Ð·Ð°ÑÐ²ÐºÐ¸ Ð¿Ð¾ ÑÐ°Ð±Ð»Ð¾Ð½Ñ
        return super().run(input)
