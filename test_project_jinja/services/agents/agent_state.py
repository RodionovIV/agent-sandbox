from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    test_task: str
    test_result: str
    test2_task: str
    test2_result: str