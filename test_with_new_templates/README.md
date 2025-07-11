# Проект: TennisMatchPrediction

## Описание

Система прогнозирования исходов теннисных матчей

## Структура каталогов
```
test_with_new_templates
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── analyzer_agent.py
│   │   ├── graph.py
│   │   └── orchestrator_agent.py
│   └── mcp
│       ├── mcp_client.py
│       └── server1_mcp.py
└── settings.py

6 directories, 9 files

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