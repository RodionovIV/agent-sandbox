import inspect
from typing import Literal

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.DataAnalyzer_agents import DataanalyzerAgent
from services.agents.DashboardSender_agents import DashboardsenderAgent


def DataAnalyzer_node(agent):
    async def create_node(state:AgentState)->Command[Literal["DashboardSender"]]:
        node_name = "DataAnalyzer_node"
        task_field = "DataAnalyzer_task"
        result_field = "DataAnalyzer_result"
        state["previous"] = "DataAnalyzer"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "DashboardSender"
        if goto == END:
            new_state["result"] = new_state["result_field"]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def DashboardSender_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "DashboardSender_node"
        task_field = "DashboardSender_task"
        result_field = "DashboardSender_result"
        state["previous"] = "DashboardSender"
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
    _DataAnalyzer_agent = await DataanalyzerAgent.create()
    _DashboardSender_agent = await DashboardsenderAgent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("DataAnalyzer")
    builder.add_node("DataAnalyzer", DataAnalyzer_node(_DataAnalyzer_agent))
    builder.add_node("DashboardSender", DashboardSender_node(_DashboardSender_agent))
    graph = builder.compile()
    return graph