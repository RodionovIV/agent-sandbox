# Ð£ÑÐ¸Ð»Ð¸ÑÑ Ð´Ð»Ñ Ð°Ð³ÐµÐ½ÑÐ¾Ð²
import json


def load_config(config_path):
    with open(config_path, "r") as f:
        return json.load(f)
