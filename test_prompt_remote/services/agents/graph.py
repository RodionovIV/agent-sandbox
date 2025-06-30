import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.orchestrator_agents import OrchestratorAgent
from services.agents.teacher_agents import TeacherAgent
from services.agents.trainer_agents import TrainerAgent

def orchestrator_node(agent):
    async def create_node(state:AgentState)->Command[Literal["teacher", "trainer", "END"]]:
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



def teacher_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "teacher_node"
        task_field = "teacher_task"
        result_field = "teacher_result"
        state["previous"] = "teacher"
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



def trainer_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "trainer_node"
        task_field = "trainer_task"
        result_field = "trainer_result"
        state["previous"] = "trainer"
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
    _teacher_agent = await TeacherAgent.create()
    _trainer_agent = await TrainerAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("orchestrator")
    builder.add_node("orchestrator", orchestrator_node(_orchestrator_agent))
    builder.add_node("teacher", teacher_node(_teacher_agent))
    builder.add_node("trainer", trainer_node(_trainer_agent))
    graph = builder.compile()
    return graph