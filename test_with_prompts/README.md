# Проект: LanguageLearningPlatform

## Описание

Платформа для изучения иностранных языков с использованием агентов

## Структура каталогов
```
test_with_prompts
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── AssistantAgent_agent.py
│   │   ├── TeacherAgent_agent.py
│   │   ├── TutorAgent_agent.py
│   │   ├── agent_state.py
│   │   └── graph.py
│   └── mcp
│       ├── mcp_client.py
│       └── server1_mcp.py
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