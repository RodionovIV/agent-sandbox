# Проект: VoiceCopilot

## Описание

Голосовой ассистент для анализа и обработки запросов, связанных с заявками.

## Структура каталогов
```
smart
├── api
│   └── endpoints.py
├── models
│   └── agents.py
├── services
│   ├── agents
│   │   ├── AgentAnalyzer_agent.py
│   │   ├── AgentCoordinator_agent.py
│   │   ├── Chat_agent.py
│   │   ├── TicketSystem_agent.py
│   │   ├── VOICECOPILOT_agent.py
│   │   ├── agent_state.py
│   │   └── graph.py
│   └── mcp
│       ├── api_server_mcp.py
│       ├── mcp_client.py
│       └── rag_server_mcp.py
└── settings.py

6 directories, 13 files

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