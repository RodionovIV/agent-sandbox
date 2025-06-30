import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.orchestrator_agents import OrchestratorAgent
from services.agents.translator_agents import TranslatorAgent
from services.agents.tutor_agents import TutorAgent

def orchestrator_node(agent):
    async def create_node(state:AgentState)->Command[Literal["translator", "tutor", "END"]]:
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



def translator_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "translator_node"
        task_field = "translator_task"
        result_field = "translator_result"
        state["previous"] = "translator"
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



def tutor_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "tutor_node"
        task_field = "tutor_task"
        result_field = "tutor_result"
        state["previous"] = "tutor"
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
    _translator_agent = await TranslatorAgent.create()
    _tutor_agent = await TutorAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("orchestrator")
    builder.add_node("orchestrator", orchestrator_node(_orchestrator_agent))
    builder.add_node("translator", translator_node(_translator_agent))
    builder.add_node("tutor", tutor_node(_tutor_agent))
    graph = builder.compile()
    return graph