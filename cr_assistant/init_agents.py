from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from agents.receiver import ReceiverAgent
from agents.analyzer import AnalyzerAgent
from agents.formatter import FormatterAgent
from agents.executor import ExecutorAgent
from agents.orchestrator import OrchestratorAgent
from agents.validator import ValidatorAgent
from tools.rag import RAGTool
from tools.sberchat import SberchatTool
from tools.jira import JiraTool
from config.config import Config

# ÐÐ°ÑÑÑÐ¾Ð¹ÐºÐ° LLM
llm = ChatOpenAI(temperature=0)

# ÐÐ°ÑÑÑÐ¾Ð¹ÐºÐ° Ð¸Ð½ÑÑÑÑÐ¼ÐµÐ½ÑÐ¾Ð²
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(Config.FAISS_INDEX_PATH, embeddings)
rag_tool = RAGTool(embeddings, vectorstore)
sberchat_tool = SberchatTool()
jira_tool = JiraTool()

# ÐÐ½Ð¸ÑÐ¸Ð°Ð»Ð¸Ð·Ð°ÑÐ¸Ñ Ð°Ð³ÐµÐ½ÑÐ¾Ð²
receiver_agent = ReceiverAgent([sberchat_tool], llm)
analyzer_agent = AnalyzerAgent([jira_tool], llm)
formatter_agent = FormatterAgent([rag_tool], llm)
executor_agent = ExecutorAgent([jira_tool], llm)
orchestrator_agent = OrchestratorAgent(
    [receiver_agent, analyzer_agent, formatter_agent, executor_agent], llm
)
validator_agent = ValidatorAgent(
    [receiver_agent, analyzer_agent, formatter_agent, executor_agent], llm
)
