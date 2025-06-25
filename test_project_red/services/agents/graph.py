import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.teacherAgent_agents import TeacheragentAgent
from services.agents.UI_agents import UiAgent
from services.agents.trainerAgent_agents import TraineragentAgent
from services.agents.UI_agents import UiAgent


def teacherAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["UI"]]:
        node_name = "teacherAgent_node"
        task_field = "teacherAgent_task"
        result_field = "teacherAgent_result"
        state["previous"] = "teacherAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "UI"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def UI_node(agent):
    async def create_node(state:AgentState)->Command[Literal["trainerAgent"]]:
        node_name = "UI_node"
        task_field = "UI_task"
        result_field = "UI_result"
        state["previous"] = "UI"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "trainerAgent"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def trainerAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["UI"]]:
        node_name = "trainerAgent_node"
        task_field = "trainerAgent_task"
        result_field = "trainerAgent_result"
        state["previous"] = "trainerAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "UI"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def UI_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "UI_node"
        task_field = "UI_task"
        result_field = "UI_result"
        state["previous"] = "UI"
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
    _teacherAgent_agent = await TeacheragentAgent.create()
    _UI_agent = await UiAgent.create()
    _trainerAgent_agent = await TraineragentAgent.create()
    _UI_agent = await UiAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("teacherAgent")
    builder.add_node("teacherAgent", teacherAgent_node(_teacherAgent_agent))
    builder.add_node("UI", UI_node(_UI_agent))
    builder.add_node("trainerAgent", trainerAgent_node(_trainerAgent_agent))
    builder.add_node("UI", UI_node(_UI_agent))
    graph = builder.compile()
    return graph