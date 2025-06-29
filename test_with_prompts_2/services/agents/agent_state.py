from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    translator_task: str
    translator_result: str
    tutor_task: str
    tutor_result: str
    orchestrator_task: str
    orchestrator_result: str