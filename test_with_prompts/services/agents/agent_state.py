from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    TeacherAgent_task: str
    TeacherAgent_result: str
    AssistantAgent_task: str
    AssistantAgent_result: str
    TutorAgent_task: str
    TutorAgent_result: str