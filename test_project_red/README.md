# Проект: LearningAssistant

## Описание

Система для обучения и тренировки пользователей с помощью агентов-учителя и тренера.

## Структура каталогов
```
test_project_red
├── Dockerfile
├── README.md
├── api
│   └── endpoints.py
├── main.py
├── models
│   └── agents.py
├── requirements.txt
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   ├── orchestrator_agent.py
│   │   ├── teacherAgent_agent.py
│   │   ├── trainerAgent_agent.py
│   │   ├── translatorAgent_agent.py
│   │   └── tutorAgent_agent.py
│   └── mcp
│       ├── api_server_mcp.py
│       ├── mcp_client.py
│       ├── mcp_server_1_mcp.py
│       ├── mcp_server_2_mcp.py
│       ├── rag_server_mcp.py
│       └── web_search_server_mcp.py
└── settings.py

6 directories, 20 files

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