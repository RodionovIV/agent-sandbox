# Проект: EmailTaskForwarder

## Описание

Система для анализа входящих писем, переадресации и создания задач в Jira

## Структура каталогов
```
mail_assist
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── ForwarderAgent_agent.py
│   │   ├── ParserAgent_agent.py
│   │   ├── agent_state.py
│   │   └── graph.py
│   └── mcp
│       ├── APIServer_mcp.py
│       ├── RAGServer_mcp.py
│       ├── WebSearchServer_mcp.py
│       └── mcp_client.py
└── settings.py

6 directories, 11 files

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