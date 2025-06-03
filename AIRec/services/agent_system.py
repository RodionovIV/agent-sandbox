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
            timeout=60,
        )
        functions = []
        llm_with_functions = llm.bind_tools(functions)
        self.agent_executor = create_react_agent(
            llm_with_functions, functions, checkpointer=MemorySaver()
        )

    def select_experts(self, query: str) -> str:
        # ÐÐ¾Ð³Ð¸ÐºÐ° Ð¿Ð¾Ð´Ð±Ð¾ÑÐ° ÑÐºÑÐ¿ÐµÑÑÐ¾Ð²
        return f"ÐÐ¾Ð´Ð±Ð¾Ñ ÑÐºÑÐ¿ÐµÑÑÐ¾Ð²: {query}"

    def check_availability(self, query: str) -> str:
        # ÐÐ¾Ð³Ð¸ÐºÐ° Ð¿ÑÐ¾Ð²ÐµÑÐºÐ¸ Ð´Ð¾ÑÑÑÐ¿Ð½Ð¾ÑÑÐ¸
        return f"ÐÑÐ¾Ð²ÐµÑÐºÐ° Ð´Ð¾ÑÑÑÐ¿Ð½Ð¾ÑÑÐ¸: {query}"

    def schedule_interviews(self, query: str) -> str:
        # ÐÐ¾Ð³Ð¸ÐºÐ° Ð¿Ð»Ð°Ð½Ð¸ÑÐ¾Ð²Ð°Ð½Ð¸Ñ Ð¸Ð½ÑÐµÑÐ²ÑÑ
        return f"ÐÐ»Ð°Ð½Ð¸ÑÐ¾Ð²Ð°Ð½Ð¸Ðµ Ð¸Ð½ÑÐµÑÐ²ÑÑ: {query}"

    def create_calendar_event(self, query: str) -> str:
        # ÐÐ¾Ð³Ð¸ÐºÐ° ÑÐ¾Ð·Ð´Ð°Ð½Ð¸Ñ ÑÐ¾Ð±ÑÑÐ¸Ñ Ð² ÐºÐ°Ð»ÐµÐ½Ð´Ð°ÑÐµ
        return f"Ð¡Ð¾Ð·Ð´Ð°Ð½Ð¸Ðµ ÑÐ¾Ð±ÑÑÐ¸Ñ Ð² ÐºÐ°Ð»ÐµÐ½Ð´Ð°ÑÐµ: {query}"
