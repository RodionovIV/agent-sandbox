import inspect
import re
import json
from typing import Literal, List

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.GoalAnalyzer_agent import GoalanalyzerAgent
from services.agents.GoalResponder_agent import GoalresponderAgent

def parse_question(text: str) -> List[str]:
    """
    Извлекает все блоки JSON, заключённые в ```json ... ``` из текста.
    Возвращает список строк (каждая — отдельный блок JSON).
    """
    pattern = r"```json\s*(.*?)\s*```"
    matches = re.search(pattern, text, re.DOTALL)
    result = None
    if matches:
        result = eval(matches.group(1))
    return result


def GoalAnalyzer_node(agent):
    async def create_node(state:AgentState)->Command[Literal["GoalResponder"]]:
        node_name = "GoalAnalyzer_node"
        task_field = "GoalAnalyzer_task"
        result_field = "GoalAnalyzer_result"
        state["previous"] = "GoalAnalyzer"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "GoalResponder"
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def GoalResponder_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "GoalResponder_node"
        task_field = "GoalResponder_task"
        result_field = "GoalResponder_result"
        state["previous"] = "GoalResponder"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = END
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node


async def create_graph():
    _GoalAnalyzer_agent = GoalanalyzerAgent()
    await _GoalAnalyzer_agent.create()
    _GoalResponder_agent = GoalresponderAgent()
    await _GoalResponder_agent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("GoalAnalyzer")
    builder.add_node("GoalAnalyzer", GoalAnalyzer_node(_GoalAnalyzer_agent))
    builder.add_node("GoalResponder", GoalResponder_node(_GoalResponder_agent))
    graph = builder.compile()
    return graph