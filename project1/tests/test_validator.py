from unittest.mock import patch
from app.agents.validator import ValidatorAgent

def test_validator():
    mock_llm = Mock(return_value={"choices": ["корректен"]})
    with patch.object(GigaChat, "__call__", side_effect=mock_llm):
        validator = ValidatorAgent()
        assert validator.validate("Ответ на запрос") == True
    