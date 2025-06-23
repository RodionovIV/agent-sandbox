from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    main_agent_task: str
    main_agent_result: str