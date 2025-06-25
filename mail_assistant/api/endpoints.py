from fastapi import APIRouter
from models.agent import AgentRequest, AgentResponse
from services.agent_system import AnalyzerAgent, RedirectorAgent

router = APIRouter()
analyzer = AnalyzerAgent()
redirector = RedirectorAgent()


@router.post("/analyze", response_model=AgentResponse)
def analyze_email(request: AgentRequest):
    result = analyzer.analyze_email(request.query)
    return AgentResponse(result=result)


@router.post("/redirect", response_model=AgentResponse)
def redirect_email(request: AgentRequest):
    result = redirector.redirect_email(request.query)
    return AgentResponse(result=result)
