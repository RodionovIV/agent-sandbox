# Ð ÐµÐ°Ð»Ð¸Ð·Ð°ÑÐ¸Ñ LLM-ÐºÐ»Ð¸ÐµÐ½ÑÐ°
import openai


class LLMClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=150
        )
        return response.choices[0].text.strip()
