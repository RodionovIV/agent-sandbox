from unittest.mock import patch
from app.agents.responder import ResponderAgent

def test_responder():
    mock_llm = Mock(return_value={"choices": ["Ответ на запрос"]})
    with patch.object(GigaChat, "__call__", side_effect=mock_llm):
        responder = ResponderAgent()
        assert responder.generate_answer("Проблема с сервером") == "Ответ на запрос"
    