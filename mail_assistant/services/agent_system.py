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


class AnalyzerAgent:
    def __init__(self):
        llm = GigaChat(
            model="GigaChat-2-Max",
            verify_ssl_certs=False,
            profanity_check=False,
            streaming=False,
            max_tokens=8192,
            temperature=0.3,
            repetition_penalty=1.01,
            timeout=60,
        )
        example_docs = [
            "ÐÐ¾Ð³Ð¾Ð´Ð° Ð² ÐÐ¡Ð Ð¿Ð°ÑÐ¼ÑÑÐ½Ð°Ñ",
            "Ð¡Ð»Ð¾Ð½ ÐºÑÐ¿Ð¸Ð» Ð²ÐµÐ»Ð¾ÑÐ¸Ð¿ÐµÐ´",
            "Bombini Gussini la brateelo Bombordiro Crocodilo",
        ]
        embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        docs = [Document(page_content=text) for text in example_docs]
        vectorstore = FAISS.from_documents(docs, embedding)
        retriver = vectorstore.as_retriever()

        self.rag_chain = RetrievalQA.from_chain_type(
            llm=llm, retriever=retriever, return_source_documents=True
        )
        functions = [rag_search]
        llm_with_functions = llm.bind_tools(functions)
        self.agent_executor = create_react_agent(
            llm_with_functions, functions, checkpointer=MemorySaver()
        )

    def analyze_email(self, email):
        # ÐÐ½Ð°Ð»Ð¸Ð· Ð¿Ð¸ÑÑÐ¼Ð°
        result = self.agent_executor.invoke(email)
        return result


class RedirectorAgent:
    def __init__(self):
        self.jira_tool = JiraTool()
        self.email_tool = EmailTool()

    def redirect_email(self, email, assignee):
        # ÐÑÐ¿ÑÐ°Ð²ÐºÐ° Ð¿Ð¸ÑÑÐ¼Ð°
        self.email_tool.send_email(email, assignee)
        # Ð¤Ð¸ÐºÑÐ°ÑÐ¸Ñ Ð·Ð°Ð´Ð°ÑÐ¸ Ð² Jira
        self.jira_tool.create_task(email, assignee)
