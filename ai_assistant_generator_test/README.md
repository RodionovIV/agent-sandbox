# Проект: LLMService

## Описание

Сервис на базе FastAPI для взаимодействия с LLM-агентами, использующими библиотеку LangChain и GigaChat.

## Структура каталогов
```
ai_assistant_generator_test
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   └── main_agent_agent.py
│   └── mcp
│       ├── mcp_client.py
│       └── rag_server_mcp.py
└── settings.py

5 directories, 8 files

```
## Описание каталогов

**api** - содержит эндпоинты, которые служат триггером запуска агента

**model** - содержит структуру входных запросов и ответов

**services/agents** - содержит классы агентов и собранный из них граф

**services/mcp** - содержит MCP серверы и MCP клиент

**main.py** - файл приложения

**settings.py** - файл конфигурации

**.env** - переменные окружения

## Запуск приложения
```
python3.11 -m venv venv
source venv/bin/activate
python -m pip install requirements.txt
python main.py
```