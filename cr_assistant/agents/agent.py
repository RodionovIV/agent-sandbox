from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool


class BaseAgent:
    def __init__(self, tools: list[BaseTool], llm: ChatOpenAI):
        self.tools = tools
        self.llm = llm
        self.agent = initialize_agent(
            tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
        )

    def run(self, input: str) -> str:
        return self.agent.run(input)
