from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    orchestrator_task: str
    orchestrator_result: str
    teacher_task: str
    teacher_result: str
    trainer_task: str
    trainer_result: str