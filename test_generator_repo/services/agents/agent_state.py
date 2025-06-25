from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    orchestrator_task: str
    orchestrator_result: str
    teacherAgent_task: str
    teacherAgent_result: str
    translatorAgent_task: str
    translatorAgent_result: str
    tutorAgent_task: str
    tutorAgent_result: str