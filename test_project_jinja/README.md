# Проект: TEST_PROJECT

## Описание

Тестовое описание

## Структура каталогов
```
/media/ts777/Kingston/Sandbox/agent-sandbox/test_project_jinja
├── api
│   └── endpoints.py
├── Dockerfile
├── main.py
├── models
│   └── agents.py
├── README.md
├── requirements.txt
├── services
│   ├── agents
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   ├── test2_agent.py
│   │   └── test_agent.py
│   └── mcp
│       ├── mcp_client.py
│       └── mcp_server.py
└── settings.py

5 directories, 13 files

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