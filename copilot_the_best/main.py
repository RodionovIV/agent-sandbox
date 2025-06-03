from fastapi import FastAPI, APIRouter
from .api.endpoints import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")
