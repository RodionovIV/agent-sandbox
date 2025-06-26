from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    parserAgent_task: str
    parserAgent_result: str
    cleanerAgent_task: str
    cleanerAgent_result: str