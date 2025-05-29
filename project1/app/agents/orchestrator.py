from .classifier import ClassifierAgent
from .responder import ResponderAgent
from .validator import ValidatorAgent

class OrchestratorAgent:
    def __init__(self):
        self.classifier = ClassifierAgent()
        self.responder = ResponderAgent()
        self.validator = ValidatorAgent()

    async def handle_request(self, request_content):
        classification_result = await self.classifier.classify(request_content)
        if classification_result == "technical":
            answer = await self.responder.generate_answer(request_content)
            validation_result = await self.validator.validate(answer)
            return validation_result
        else:
            raise ValueError("Unknown request type.")
    