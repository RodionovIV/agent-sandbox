# Ð¢ÐµÑÑÐ¸ÑÐ¾Ð²Ð°Ð½Ð¸Ðµ Ð°Ð³ÐµÐ½ÑÐ°
from agents.agent import Agent


def test_agent():
    agent = Agent("data/sample_data.json")
    assert agent.config["tools"] == ["search", "calculator", "translator"]


if __name__ == "__main__":
    test_agent()
