# Проект: EducationalAssistant

## Описание

Интеллектуальная система для создания уроков, перевода и проверки заданий.

## Структура каталогов
```
test_generator_repo
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── Assistant_agent.py
│   │   ├── Evaluator_agent.py
│   │   ├── Teacher_agent.py
│   │   ├── agent_state.py
│   │   ├── graph.py
│   │   ├── orchestrator_agent.py
│   │   ├── teacherAgent_agent.py
│   │   ├── translatorAgent_agent.py
│   │   └── tutorAgent_agent.py
│   └── mcp
│       ├── ExternalResources_mcp.py
│       ├── ExternalSystems_mcp.py
│       ├── mcp_client.py
│       ├── server1_mcp.py
│       └── server2_mcp.py
└── settings.py

6 directories, 17 files

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