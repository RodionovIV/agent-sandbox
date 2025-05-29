from unittest.mock import patch
from app.agents.classifier import ClassifierAgent

def test_classifier():
    mock_llm = Mock(return_value={"choices": ["technical"]})
    with patch.object(GigaChat, "__call__", side_effect=mock_llm):
        classifier = ClassifierAgent()
        assert classifier.classify("Проблема с сервером") == "technical"
    