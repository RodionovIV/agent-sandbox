import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.TeacherAgent_agents import TeacheragentAgent
from services.agents.AssistantAgent_agents import AssistantagentAgent
from services.agents.TutorAgent_agents import TutoragentAgent


def TeacherAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["AssistantAgent"]]:
        node_name = "TeacherAgent_node"
        task_field = "TeacherAgent_task"
        result_field = "TeacherAgent_result"
        state["previous"] = "TeacherAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "AssistantAgent"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def AssistantAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["TutorAgent"]]:
        node_name = "AssistantAgent_node"
        task_field = "AssistantAgent_task"
        result_field = "AssistantAgent_result"
        state["previous"] = "AssistantAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "TutorAgent"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def TutorAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "TutorAgent_node"
        task_field = "TutorAgent_task"
        result_field = "TutorAgent_result"
        state["previous"] = "TutorAgent"
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
    _TeacherAgent_agent = await TeacheragentAgent.create()
    _AssistantAgent_agent = await AssistantagentAgent.create()
    _TutorAgent_agent = await TutoragentAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("TeacherAgent")
    builder.add_node("TeacherAgent", TeacherAgent_node(_TeacherAgent_agent))
    builder.add_node("AssistantAgent", AssistantAgent_node(_AssistantAgent_agent))
    builder.add_node("TutorAgent", TutorAgent_node(_TutorAgent_agent))
    graph = builder.compile()
    return graph