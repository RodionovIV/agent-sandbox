from fastapi import FastAPI
from api.endpoints import router
from services.agent_system import AgentSystem

app = FastAPI()
agent = AgentSystem()
app.include_router(router)
