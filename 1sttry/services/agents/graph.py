import inspect
import re
import json
from typing import Literal, List

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.ParserAgent_agent import ParseragentAgent
from services.agents.ExecutorAgent_agent import ExecutoragentAgent

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


def ParserAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["ExecutorAgent"]]:
        node_name = "ParserAgent_node"
        task_field = "ParserAgent_task"
        result_field = "ParserAgent_result"
        state["previous"] = "ParserAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "ExecutorAgent"
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def ExecutorAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "ExecutorAgent_node"
        task_field = "ExecutorAgent_task"
        result_field = "ExecutorAgent_result"
        state["previous"] = "ExecutorAgent"
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
    _ParserAgent_agent = ParseragentAgent()
    await _ParserAgent_agent.create()
    _ExecutorAgent_agent = ExecutoragentAgent()
    await _ExecutorAgent_agent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("ParserAgent")
    builder.add_node("ParserAgent", ParserAgent_node(_ParserAgent_agent))
    builder.add_node("ExecutorAgent", ExecutorAgent_node(_ExecutorAgent_agent))
    graph = builder.compile()
    return graph