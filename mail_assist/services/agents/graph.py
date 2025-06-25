import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.ParserAgent_agents import ParseragentAgent
from services.agents.ForwarderAgent_agents import ForwarderagentAgent


def ParserAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["ForwarderAgent"]]:
        node_name = "ParserAgent_node"
        task_field = "ParserAgent_task"
        result_field = "ParserAgent_result"
        state["previous"] = "ParserAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "ForwarderAgent"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def ForwarderAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "ForwarderAgent_node"
        task_field = "ForwarderAgent_task"
        result_field = "ForwarderAgent_result"
        state["previous"] = "ForwarderAgent"
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
    _ParserAgent_agent = await ParseragentAgent.create()
    _ForwarderAgent_agent = await ForwarderagentAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("ParserAgent")
    builder.add_node("ParserAgent", ParserAgent_node(_ParserAgent_agent))
    builder.add_node("ForwarderAgent", ForwarderAgent_node(_ForwarderAgent_agent))
    graph = builder.compile()
    return graph