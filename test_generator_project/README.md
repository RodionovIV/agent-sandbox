# Проект: Заявка в систему

## Описание

Проект для обработки заявок через агентов

## Структура каталогов
```
test_generator_project
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── agent_analytic_agent.py
│   │   ├── agent_sender_agent.py
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   └── orchestrator_agent.py
│   └── mcp
│       ├── mcp_client.py
│       ├── mcp_server_1_mcp.py
│       └── mcp_server_2_mcp.py
└── settings.py

5 directories, 11 files

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