from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    ParserAgent_task: str
    ParserAgent_result: str
    ExecutorAgent_task: str
    ExecutorAgent_result: str