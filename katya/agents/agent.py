# Ð ÐµÐ°Ð»Ð¸Ð·Ð°ÑÐ¸Ñ Ð°Ð³ÐµÐ½ÑÐ°
from .tools import Tool
from .utils import load_config


class Agent:
    def __init__(self, config_path):
        self.config = load_config(config_path)
        self.tools = [Tool(name) for name in self.config["tools"]]

    def run(self, query):
        # ÐÐ¾Ð³Ð¸ÐºÐ° ÑÐ°Ð±Ð¾ÑÑ Ð°Ð³ÐµÐ½ÑÐ°
        pass
