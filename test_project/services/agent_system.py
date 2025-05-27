from langchain_gigachat.chat_models import GigaChat
from langchain_gigachat.tools.giga_tool import giga_tool

from langchain.schema import HumanMessage, SystemMessage, Document, AIMessage
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Optional, Literal, List, Dict
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

from pathlib import Path
import time
import datetime
import warnings
import os
import re

class AgentSystem:
    def __init__(self):
        llm = GigaChat(
            model="GigaChat-2-Max",
            verify_ssl_certs=False,
            profanity_check=False,
            streaming=False,
            max_tokens=8192,
            temperature=0.3,
            repetition_penalty=1.01,
            timeout=60
        )
        functions = [rag_search]
        llm_with_functions = llm.bind_tools(functions)
        self.agent_executor = create_react_agent(llm_with_functions, 
                                                functions,
                                                checkpointer=MemorySaver()
                                               )

    def process(self, query: str) -> str:
        message = {
            "messages": [HumanMessage(content=query)]
        }
        result = self.agent_executor.invoke(message)
        return result["result"]

class RagTool:
    def __init__(self):
        llm = GigaChat(
            model="GigaChat-2-Max",
            verify_ssl_certs=False,
            profanity_check=False,
            streaming=False,
            max_tokens=8192,
            temperature=0.3,
            repetition_penalty=1.01,
            timeout=60
        )
        example_docs = [
            "Погода в МСК пасмурная",
            "Слон купил велосипед",
            "Bombini Gussini la brateelo Bombordiro Crocodilo"
        ]
        embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        docs = [Document(page_content=text) for text in example_docs]
        vectorstore = FAISS.from_documents(docs, embedding)
        retriver = vectorstore.as_retriever()

        self.rag_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )

    def run_tool(self, query):
        _query = {"query": query}
        result = self.rag_chain.invoke(_query)["result"]
        return result

class RagResult(BaseModel):
    status: str = Field(description="Статус исполнения RAG")
    message: str = Field(description="Сообщение о результате исполнения RAG")
    result: str = Field(description="Результат исполнения RAG")

few_shot_examples_rag = [
    {
        "request": "Сколько лет Льву Николаевичу Толстому?",
        "params": {"query": "Сколько лет Льву Николаевичу Толстому?"},
    }
]

@giga_tool(few_shot_examples=few_shot_examples_rag)
def rag_search(
    query: str = Field(description="Запрос в векторную БД для RAG")
) -> RagResult:
    """Использование поиска"""
    print(f"! rag_search with query: {query}")
    try:
        result = rag_chain.run_tool(query)
        return RagResult(status="OK", message="Ответ получен!", result=result)
    except Exception as e:
        return RagResult(status="FAIL", message=f"Не удалось запустить инструмент, ошибка: {e}", result=None)