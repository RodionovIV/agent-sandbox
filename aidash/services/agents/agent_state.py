from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    DataAnalyzer_task: str
    DataAnalyzer_result: str
    DashboardSender_task: str
    DashboardSender_result: str