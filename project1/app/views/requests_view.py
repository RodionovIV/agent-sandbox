from fastapi import APIRouter
from ..models.request import RequestCreateSchema
from ..core.db_service import get_db_session
from ..core.agent_system import AgentSystem

router = APIRouter()

@router.post("/", response_model=str)
async def send_request(request_data: RequestCreateSchema):
    session = next(get_db_session())
    new_request = Request(**request_data.dict())
    session.add(new_request)
    session.commit()
    processed_response = await AgentSystem().process_request(request_data.content)
    return processed_response
    