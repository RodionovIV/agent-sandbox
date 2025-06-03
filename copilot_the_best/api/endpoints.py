from fastapi import APIRouter
from ..models.agent import AgentRequest, AgentResponse
from ..services.agent_system import AgentSystem

router = APIRouter()

agent = AgentSystem()


@router.post("/agent", response_model=AgentResponse)
def process_agent_request(request: AgentRequest):
    result = agent.process(request.query)
    return AgentResponse(result=result)
