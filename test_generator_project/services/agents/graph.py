import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.orchestrator_agents import OrchestratorAgent
from services.agents.agent_analytic_agents import Agent_analyticAgent
from services.agents.agent_sender_agents import Agent_senderAgent

def orchestrator_node(agent):
    async def create_node(state:AgentState)->Command[Literal["agent_analytic", "agent_sender", "END"]]:
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



def agent_analytic_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "agent_analytic_node"
        task_field = "agent_analytic_task"
        result_field = "agent_analytic_result"
        state["previous"] = "agent_analytic"
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



def agent_sender_node(agent):
    async def create_node(state:AgentState)->Command[Literal["orchestrator"]]:
        node_name = "agent_sender_node"
        task_field = "agent_sender_task"
        result_field = "agent_sender_result"
        state["previous"] = "agent_sender"
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
    _agent_analytic_agent = await Agent_analyticAgent.create()
    _agent_sender_agent = await Agent_senderAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("orchestrator")
    builder.add_node("orchestrator", orchestrator_node(_orchestrator_agent))
    builder.add_node("agent_analytic", agent_analytic_node(_agent_analytic_agent))
    builder.add_node("agent_sender", agent_sender_node(_agent_sender_agent))
    graph = builder.compile()
    return graph