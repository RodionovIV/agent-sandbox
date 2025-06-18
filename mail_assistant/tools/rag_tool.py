from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document


class RAGTool:
    def __init__(self):
        example_docs = [
            "ÐÐ¾Ð³Ð¾Ð´Ð° Ð² ÐÐ¡Ð Ð¿Ð°ÑÐ¼ÑÑÐ½Ð°Ñ",
            "Ð¡Ð»Ð¾Ð½ ÐºÑÐ¿Ð¸Ð» Ð²ÐµÐ»Ð¾ÑÐ¸Ð¿ÐµÐ´",
            "Bombini Gussini la brateelo Bombordiro Crocodilo",
        ]
        embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        docs = [Document(page_content=text) for text in example_docs]
        self.vectorstore = FAISS.from_documents(docs, embedding)

    def search(self, query):
        return self.vectorstore.similarity_search(query)
