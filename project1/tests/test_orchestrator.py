from unittest.mock import patch
from app.agents.orchestrator import OrchestratorAgent

def test_orchestrator():
    mock_classifier = Mock(return_value="technical")
    mock_responder = Mock(return_value="Ответ на запрос")
    mock_validator = Mock(return_value=True)

    with patch.object(OrchestratorAgent, "classifier", mock_classifier), \
         patch.object(OrchestratorAgent, "responder", mock_responder), \
         patch.object(OrchestratorAgent, "validator", mock_validator):
        orchestrator = OrchestratorAgent()
        result = orchestrator.handle_request("Проблема с сервером")
        assert result == True
    