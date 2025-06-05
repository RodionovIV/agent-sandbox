from langchain.tools import BaseTool


class SberchatTool(BaseTool):
    name = "SberchatTool"
    description = "Tool for interacting with Sberchat"

    def _run(self, query: str) -> str:
        # ÐÐ·Ð°Ð¸Ð¼Ð¾Ð´ÐµÐ¹ÑÑÐ²Ð¸Ðµ Ñ ÐºÐ¾ÑÐ¿Ð¾ÑÐ°ÑÐ¸Ð²Ð½ÑÐ¼ Ð¼ÐµÑÑÐµÐ½Ð´Ð¶ÐµÑÐ¾Ð¼ Ð¡Ð±ÐµÑÑÐ°Ñ
        return "Response from Sberchat"
