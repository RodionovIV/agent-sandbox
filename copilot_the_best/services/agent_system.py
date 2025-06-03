from langchain_gigachat.chat_models import GigaChat
from langchain_gigachat.tools.giga_tool import giga_tool
from langchain.schema import HumanMessage, SystemMessage, Document, AIMessage
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver


class AgentSystem:
    def __init__(self):
        self.llm = GigaChat(
            model="GigaChat-2-Max",
            verify_ssl_certs=False,
            profanity_check=False,
            streaming=False,
            max_tokens=8192,
            temperature=0.3,
            repetition_penalty=1.01,
            timeout=60,
        )

        functions = [rag_search]
        self.llm_with_functions = self.llm.bind_tools(functions)

        self.agent_executor = create_react_agent(
            self.llm_with_functions, functions, checkpointer=MemorySaver()
        )

    def process(self, query: str) -> str:
        config = {"configurable": {"thread_id": "thread_id4"}}
        message = {"messages": [HumanMessage(content=query)]}
        result = self.agent_executor.invoke(message, config=config)
        return result


# ÐÑÐ¸Ð¼ÐµÑ ÑÑÐ½ÐºÑÐ¸Ð¸ Ð´Ð»Ñ Ð¿Ð¾Ð¸ÑÐºÐ° Ð² RAG
def rag_search(query: str) -> str:
    # Ð ÐµÐ°Ð»Ð¸Ð·Ð°ÑÐ¸Ñ Ð¿Ð¾Ð¸ÑÐºÐ° Ð² RAG
    return "ÐÑÐ¸Ð¼ÐµÑ Ð¾ÑÐ²ÐµÑÐ° Ð¾Ñ RAG"
