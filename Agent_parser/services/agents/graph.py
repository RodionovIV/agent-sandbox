import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.parserAgent_agents import ParseragentAgent
from services.agents.cleanerAgent_agents import CleaneragentAgent


def parserAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["cleanerAgent"]]:
        node_name = "parserAgent_node"
        task_field = "parserAgent_task"
        result_field = "parserAgent_result"
        state["previous"] = "parserAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "cleanerAgent"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def cleanerAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "cleanerAgent_node"
        task_field = "cleanerAgent_task"
        result_field = "cleanerAgent_result"
        state["previous"] = "cleanerAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = END
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node


async def create_graph():
    _parserAgent_agent = await ParseragentAgent.create()
    _cleanerAgent_agent = await CleaneragentAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("parserAgent")
    builder.add_node("parserAgent", parserAgent_node(_parserAgent_agent))
    builder.add_node("cleanerAgent", cleanerAgent_node(_cleanerAgent_agent))
    graph = builder.compile()
    return graph