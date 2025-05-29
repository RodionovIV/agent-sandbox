from fastapi import FastAPI
from app.views.requests_view import router as requests_router
from app.views.answers_view import router as answers_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    pass  # здесь можем инициализировать базу данных и другие ресурсы

@app.on_event("shutdown")
async def shutdown():
    pass  # закрываем соединения и освобождаем ресурсы

app.include_router(requests_router, prefix="/requests", tags=["Requests"])
app.include_router(answers_router, prefix="/answers", tags=["Answers"])
    