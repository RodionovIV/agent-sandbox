from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from agents.agent import BaseAgent


class ExecutorAgent(BaseAgent):
    def __init__(self, tools: list[BaseTool], llm: ChatOpenAI):
        super().__init__(tools, llm)

    def run(self, input: str) -> str:
        # ÐÑÐ¿ÑÐ°Ð²ÐºÐ° Ð·Ð°ÑÐ²ÐºÐ¸ Ð² Jira
        return super().run(input)
