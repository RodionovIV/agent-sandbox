from .agents.orchestrator import OrchestratorAgent

class AgentSystem:
    def __init__(self):
        self.orchestrator = OrchestratorAgent()

    async def process_request(self, request_content):
        return await self.orchestrator.handle_request(request_content)
    