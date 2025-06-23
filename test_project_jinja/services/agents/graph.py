import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.test_agents import TestAgent
from services.agents.test2_agents import Test2Agent


def test_node(agent):
    async def create_node(state:AgentState)->Command[Literal["test2"]]:
        node_name = inspect.currentframe().f_code.co_name
        task_field = "test_task"
        result_field = "test_result"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "test2"
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def test2_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = inspect.currentframe().f_code.co_name
        task_field = "test2_task"
        result_field = "test2_result"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = END
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node


async def create_graph():
    _test_agent = await TestAgent.create()
    _test2_agent = await Test2Agent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("test")
    builder.add_node("test", test_node(_test_agent))
    builder.add_node("test2", test2_node(_test2_agent))
    graph = builder.compile()
    return graph