from fastapi import APIRouter
from models.agent import AgentRequest, AgentResponse
from services.agent_system import AgentSystem

router = APIRouter()
agent = AgentSystem()


@router.post("/select_experts", response_model=AgentResponse)
def select_experts(request: AgentRequest):
    result = agent.select_experts(request.query)
    return AgentResponse(result=result)


@router.post("/check_availability", response_model=AgentResponse)
def check_availability(request: AgentRequest):
    result = agent.check_availability(request.query)
    return AgentResponse(result=result)


@router.post("/schedule_interviews", response_model=AgentResponse)
def schedule_interviews(request: AgentRequest):
    result = agent.schedule_interviews(request.query)
    return AgentResponse(result=result)


@router.post("/create_calendar_event", response_model=AgentResponse)
def create_calendar_event(request: AgentRequest):
    result = agent.create_calendar_event(request.query)
    return AgentResponse(result=result)
