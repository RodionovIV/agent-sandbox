from langchain_gigachat.chat_models import GigaChat
from langchain.prompts import PromptTemplate

class ResponderAgent:
    def __init__(self):
        self.llm = GigaChat(model="GigaChat-2-Max")
        self.prompt_template = PromptTemplate(
            input_variables=["content"],
            template="На основе следующего текста дайте ответ:\n\n{content}\nОтвет:"
        )

    async def generate_answer(self, content):
        prompt = self.prompt_template.format(content=content)
        response = self.llm([HumanMessage(content=prompt)])
        return response.content.strip()
    