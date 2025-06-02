from fastapi import APIRouter

router = APIRouter()


@router.post("/process")
def process_query(query: str):
    # ÐÐ¾Ð³Ð¸ÐºÐ° Ð¾Ð±ÑÐ°Ð±Ð¾ÑÐºÐ¸ Ð·Ð°Ð¿ÑÐ¾ÑÐ°
    return {"response": "Processed query: " + query}
