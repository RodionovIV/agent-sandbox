import inspect
import re
import json
from typing import Literal, List

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from services.agents.agent_state import AgentState
from services.agents.VOICECOPILOT_agent import VoicecopilotAgent
from services.agents.AgentAnalyzer_agent import AgentanalyzerAgent
from services.agents.AgentCoordinator_agent import AgentcoordinatorAgent
from services.agents.Chat_agent import ChatAgent
from services.agents.TicketSystem_agent import TicketsystemAgent

def parse_question(text: str) -> List[str]:
    """
    Извлекает все блоки JSON, заключённые в ```json ... ``` из текста.
    Возвращает список строк (каждая — отдельный блок JSON).
    """
    pattern = r"```json\s*(.*?)\s*```"
    matches = re.search(pattern, text, re.DOTALL)
    result = None
    if matches:
        result = eval(matches.group(1))
    return result


def VOICECOPILOT_node(agent):
    async def create_node(state:AgentState)->Command[Literal["AgentAnalyzer"]]:
        node_name = "VOICECOPILOT_node"
        task_field = "VOICECOPILOT_task"
        result_field = "VOICECOPILOT_result"
        state["previous"] = "VOICECOPILOT"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "AgentAnalyzer"
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def AgentAnalyzer_node(agent):
    async def create_node(state:AgentState)->Command[Literal["AgentCoordinator"]]:
        node_name = "AgentAnalyzer_node"
        task_field = "AgentAnalyzer_task"
        result_field = "AgentAnalyzer_result"
        state["previous"] = "AgentAnalyzer"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "AgentCoordinator"
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def AgentCoordinator_node(agent):
    async def create_node(state:AgentState)->Command[Literal["Chat"]]:
        node_name = "AgentCoordinator_node"
        task_field = "AgentCoordinator_task"
        result_field = "AgentCoordinator_result"
        state["previous"] = "AgentCoordinator"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "Chat"
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def Chat_node(agent):
    async def create_node(state:AgentState)->Command[Literal["TicketSystem"]]:
        node_name = "Chat_node"
        task_field = "Chat_task"
        result_field = "Chat_result"
        state["previous"] = "Chat"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = "TicketSystem"
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node



def TicketSystem_node(agent):
    async def create_node(state:AgentState)->Command[Literal[END]]:
        node_name = "TicketSystem_node"
        task_field = "TicketSystem_task"
        result_field = "TicketSystem_result"
        state["previous"] = "TicketSystem"
        print(f"Status: {node_name}")

        new_state = await agent.run_agent(state)

        goto = END
        if goto == END:
            new_state["result"] = new_state[result_field]
        return Command(
            update={
                k:v for k, v in new_state.items()
            },
            goto=goto
        )
    return create_node


async def create_graph():
    _VOICECOPILOT_agent = VoicecopilotAgent()
    await _VOICECOPILOT_agent.create()
    _AgentAnalyzer_agent = AgentanalyzerAgent()
    await _AgentAnalyzer_agent.create()
    _AgentCoordinator_agent = AgentcoordinatorAgent()
    await _AgentCoordinator_agent.create()
    _Chat_agent = ChatAgent()
    await _Chat_agent.create()
    _TicketSystem_agent = TicketsystemAgent()
    await _TicketSystem_agent.create()
    builder = StateGraph(state_schema=AgentState)
    builder.set_entry_point("VOICECOPILOT")
    builder.add_node("VOICECOPILOT", VOICECOPILOT_node(_VOICECOPILOT_agent))
    builder.add_node("AgentAnalyzer", AgentAnalyzer_node(_AgentAnalyzer_agent))
    builder.add_node("AgentCoordinator", AgentCoordinator_node(_AgentCoordinator_agent))
    builder.add_node("Chat", Chat_node(_Chat_agent))
    builder.add_node("TicketSystem", TicketSystem_node(_TicketSystem_agent))
    graph = builder.compile()
    return graph