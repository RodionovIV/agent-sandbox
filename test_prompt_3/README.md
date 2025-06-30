# Проект: LanguageLearningAssistant

## Описание

Система для изучения иностранных языков с использованием агентов-переводчика и учителя, координируемых оркестратором.

## Структура каталогов
```
test_prompt_3
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   ├── orchestrator_agent.py
│   │   ├── translator_agent.py
│   │   └── tutor_agent.py
│   └── mcp
│       ├── mcp_client.py
│       ├── translation_server_mcp.py
│       └── tutoring_server_mcp.py
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