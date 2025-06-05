from langchain.tools import BaseTool


class JiraTool(BaseTool):
    name = "JiraTool"
    description = "Tool for interacting with Jira"

    def _run(self, query: str) -> str:
        # ÐÐ·Ð°Ð¸Ð¼Ð¾Ð´ÐµÐ¹ÑÑÐ²Ð¸Ðµ Ñ Jira
        return "Response from Jira"
