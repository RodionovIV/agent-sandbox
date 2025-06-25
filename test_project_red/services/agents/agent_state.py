from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    teacherAgent_task: str
    teacherAgent_result: str
    trainerAgent_task: str
    trainerAgent_result: str