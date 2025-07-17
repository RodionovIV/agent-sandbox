# Проект: GoalValidationSystem

## Описание

Система для проверки целей компании на соответствие критериям SMART и формирования ответа пользователю.

## Структура каталогов
```
target
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── GoalAnalyzer_agent.py
│   │   ├── GoalResponder_agent.py
│   │   ├── agent_state.py
│   │   └── graph.py
│   └── mcp
│       └── mcp_client.py
└── settings.py

6 directories, 8 files

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