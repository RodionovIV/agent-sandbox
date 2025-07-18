# Проект: Adaptation Process Automation

## Описание

Автоматизация процесса адаптации сотрудников с использованием агентов для извлечения данных и подачи заявок.

## Структура каталогов
```
1sttry
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── ExecutorAgent_agent.py
│   │   ├── ParserAgent_agent.py
│   │   ├── agent_state.py
│   │   └── graph.py
│   └── mcp
│       ├── confluence_server_mcp.py
│       ├── mcp_client.py
│       ├── pulse_server_mcp.py
│       ├── sberdru_server_mcp.py
│       └── sberusersoft_server_mcp.py
└── settings.py

6 directories, 12 files

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