from fastapi import APIRouter
from ..models.answer import AnswerSchema
from ..core.db_service import get_db_session

router = APIRouter()

@router.get("/{request_id}/response", response_model=AnswerSchema)
async def get_answer(request_id: int):
    session = next(get_db_session())
    answer = session.query(Answer).filter_by(request_id=request_id).first()
    return answer
    