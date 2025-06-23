import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.orchestrator_agents import OrchestratorAgent
from services.agents.teacherAgent_agents import TeacheragentAgent
from services.agents.translatorAgent_agents import TranslatoragentAgent
from services.agents.tutorAgent_agents import TutoragentAgent

def orchestrator_node(agent):
    async def create_node(state:AgentState)->Command[Literal["teacherAgent", "translatorAgent", "tutorAgent", "END"]]:
        node_name = "orchestrator_node"
        task_field = "orchestrator_task"
        result_field = "orchestrator_result"
        state["previous"] = "orchestrator"
        print(f"Status: {node_name}")
        for _ in range(3):
            new_state = await agent.run_agent(state)
            tmp_result = parse_question(new_state[result_field])
            if tmp_result:
                break
            else:
                new_state[result_field] = tmp_result["result"]
                goto = tmp_result["next"]
        else:
            new_state[result_field] = "FAIL"
            goto = END
        if goto == END:
            result = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def teacherAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "teacherAgent_node"
        task_field = "teacherAgent_task"
        result_field = "teacherAgent_result"
        state["previous"] = "teacherAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "orchestrator"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def translatorAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "translatorAgent_node"
        task_field = "translatorAgent_task"
        result_field = "translatorAgent_result"
        state["previous"] = "translatorAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "orchestrator"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def tutorAgent_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "tutorAgent_node"
        task_field = "tutorAgent_task"
        result_field = "tutorAgent_result"
        state["previous"] = "tutorAgent"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "orchestrator"
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
    _orchestrator_agent = await OrchestratorAgent.create()
    _teacherAgent_agent = await TeacheragentAgent.create()
    _translatorAgent_agent = await TranslatoragentAgent.create()
    _tutorAgent_agent = await TutoragentAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("orchestrator")
    builder.add_node("orchestrator", orchestrator_node(_orchestrator_agent))
    builder.add_node("teacherAgent", teacherAgent_node(_teacherAgent_agent))
    builder.add_node("translatorAgent", translatorAgent_node(_translatorAgent_agent))
    builder.add_node("tutorAgent", tutorAgent_node(_tutorAgent_agent))
    graph = builder.compile()
    return graph