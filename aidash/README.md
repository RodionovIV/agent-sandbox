# Проект: GrafanaDashboardGenerator

## Описание

Проект для генерации и передачи дашбордов в Grafana

## Структура каталогов
```
aidash
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── DashboardSender_agent.py
│   │   ├── DataAnalyzer_agent.py
│   │   ├── agent_state.py
│   │   └── graph.py
│   └── mcp
│       ├── database_server_mcp.py
│       ├── grafana_server_mcp.py
│       └── mcp_client.py
└── settings.py

6 directories, 10 files

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