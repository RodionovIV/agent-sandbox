from langchain_gigachat.chat_models import GigaChat
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

class ClassifierAgent:
    def __init__(self):
        self.llm = GigaChat(model="GigaChat-2-Max")
        self.prompt_template = PromptTemplate(
            input_variables=["content"],
            template="Определите тип данного запроса:\n\n{content}\nТип:"
        )

    def classify(self, content):
        prompt = self.prompt_template.format(content=content)
        response = self.llm([HumanMessage(content=prompt)])
        return response.content.strip().lower()  # возвращаем тип запроса
    