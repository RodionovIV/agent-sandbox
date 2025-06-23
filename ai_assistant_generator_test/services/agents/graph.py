import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.main_agent_agents import Main_agentAgent


def main_agent_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "main_agent_node"
        task_field = "main_agent_task"
        result_field = "main_agent_result"
        state["previous"] = "main_agent"
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
    _main_agent_agent = await Main_agentAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("main_agent")
    builder.add_node("main_agent", main_agent_node(_main_agent_agent))
    graph = builder.compile()
    return graph