from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    analyst_task: str
    analyst_result: str
    explainer_task: str
    explainer_result: str
    orchestrator_task: str
    orchestrator_result: str