# Проект: BusinessForecastingSystem

## Описание

Система прогнозирования бизнес-показателей с объяснением и рекомендациями.

## Структура каталогов
```
Dt
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── analyst_agent.py
│   │   ├── explainer_agent.py
│   │   ├── graph.py
│   │   └── orchestrator_agent.py
│   └── mcp
│       ├── api_server_mcp.py
│       ├── mcp_client.py
│       └── rag_server_mcp.py
└── settings.py

6 directories, 11 files

```
## Описание каталогов

**api** - содержит эндпоинты, которые служат триггером запуска агента

**model** - содержит структуру входных запросов и ответов

**services/agents** - содержит классы агентов и собранный из них граф

**services/mcp** - содержит MCP серверы и MCP клиент

**prompts/** - содержит промпты для агентов

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