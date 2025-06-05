from fastapi import APIRouter

router = APIRouter()


@router.get("/requests/{request_id}")
async def get_request(request_id: int):
    # ÐÐ¾Ð»ÑÑÐµÐ½Ð¸Ðµ Ð·Ð°ÑÐ²ÐºÐ¸
    return {"request_id": request_id}


@router.post("/requests")
async def create_request(request: dict):
    # Ð¡Ð¾Ð·Ð´Ð°Ð½Ð¸Ðµ Ð·Ð°ÑÐ²ÐºÐ¸
    return {"request_id": 1}
