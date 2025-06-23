from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    orchestrator_task: str
    orchestrator_result: str
    agent_analytic_task: str
    agent_analytic_result: str
    agent_sender_task: str
    agent_sender_result: str