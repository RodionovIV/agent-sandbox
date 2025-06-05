from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from agents.agent import BaseAgent


class ReceiverAgent(BaseAgent):
    def __init__(self, tools: list[BaseTool], llm: ChatOpenAI):
        super().__init__(tools, llm)

    def run(self, input: str) -> str:
        # ÐÑÐ¾Ð²ÐµÑÐºÐ° ÐºÐ¾ÑÑÐµÐºÑÐ½Ð¾ÑÑÐ¸ Ð·Ð°Ð¿ÑÐ¾ÑÐ°
        if not input.strip():
            return "ÐÐµÐºÐ¾ÑÑÐµÐºÑÐ½ÑÐ¹ Ð·Ð°Ð¿ÑÐ¾Ñ"
        return super().run(input)
