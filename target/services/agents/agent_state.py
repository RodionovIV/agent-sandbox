from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    GoalAnalyzer_task: str
    GoalAnalyzer_result: str
    GoalResponder_task: str
    GoalResponder_result: str