import os


class Config:
    SBERCHAT_API_KEY = os.getenv("SBERCHAT_API_KEY")
    JIRA_API_KEY = os.getenv("JIRA_API_KEY")
    FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH")
