from langchain_gigachat.chat_models import GigaChat
from langchain.prompts import PromptTemplate

class ValidatorAgent:
    def __init__(self):
        self.llm = GigaChat(model="GigaChat-2-Max")
        self.prompt_template = PromptTemplate(
            input_variables=["answer"],
            template="Оцените корректность следующего ответа:\n\n{answer}\nКорректность:"
        )

    async def validate(self, answer):
        prompt = self.prompt_template.format(answer=answer)
        response = self.llm([HumanMessage(content=prompt)])
        return response.content.strip().lower() == "корректен"
    