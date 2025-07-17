from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    VOICECOPILOT_task: str
    VOICECOPILOT_result: str
    AgentAnalyzer_task: str
    AgentAnalyzer_result: str
    AgentCoordinator_task: str
    AgentCoordinator_result: str
    Chat_task: str
    Chat_result: str
    TicketSystem_task: str
    TicketSystem_result: str