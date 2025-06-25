# Проект: EducationalAssistant

## Описание

Система для создания уроков, перевода и проверки заданий

## Структура каталогов
```
test_project_red
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   ├── orchestrator_agent.py
│   │   ├── teacherAgent_agent.py
│   │   ├── translatorAgent_agent.py
│   │   └── tutorAgent_agent.py
│   └── mcp
│       ├── api_server_mcp.py
│       ├── mcp_client.py
│       └── rag_server_mcp.py
└── settings.py

5 directories, 12 files

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