from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS


class RAGTool(BaseTool):
    name = "RAGTool"
    description = "Tool for vector search"

    def __init__(self, embeddings: SentenceTransformerEmbeddings, vectorstore: FAISS):
        super().__init__()
        self.embeddings = embeddings
        self.vectorstore = vectorstore

    def _run(self, query: str) -> str:
        # ÐÐµÐºÑÐ¾ÑÐ½ÑÐ¹ Ð¿Ð¾Ð¸ÑÐº
        docs = self.vectorstore.similarity_search(query)
        return docs[0].page_content if docs else "No results found"
