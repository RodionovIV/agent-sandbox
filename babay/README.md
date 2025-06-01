# AI помощник для изучения иностранных языков

## Описание
Проект представляет собой AI помощника для изучения иностранных языков, построенный на основе FastAPI и LLM-агентов.

## Структура проекта
```
project_name/
├── main.py                # Точка входа в приложение
├── api/
│   └── endpoints.py       # FastAPI роутеры
├── models/
│   ├── agent.py           # Pydantic модели: AgentRequest, AgentResponse
├── services/
│   └── agent_system.py    # Логика агента (AgentSystem класс)
└── dependencies/          # (необязательно) зависимости, например для DI
```

## Инструкция по запуску
1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите приложение: `uvicorn main:app --reload`

## Примеры использования
Пример запроса к агенту:
```bash
curl -X POST "http://localhost:8000/agent" -H "Content-Type: application/json" -d '{"query": "Привет, как дела?"}'
```

## Автор
Ваше имя