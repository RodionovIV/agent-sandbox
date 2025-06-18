# Mail Assistant

Проект представляет собой систему на основе агентов, которая анализирует входящие письма, формирует резюме задачи и переадресует письмо ответственному сотруднику, фиксируя задачу в Jira.

## Структура проекта

```
.
├── api
│   ├── endpoints.py
│   └── __init__.py
├── main.py
├── models
│   ├── agent.py
│   └── __init__.py
├── services
│   ├── agent_system.py
│   └── __init__.py
├── tools
│   ├── email_tool.py
│   ├── jira_tool.py
│   ├── rag_tool.py
│   └── __init__.py
├── README.md
└── requirements.txt
```

## Инструкция по запуску

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Запустите приложение:

```bash
uvicorn main:app --reload
```

3. Используйте API для анализа и переадресации писем.

## Примеры использования

### Анализ письма

```bash
curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"query": "Тема письма"}'
```

### Переадресация письма

```bash
curl -X POST http://localhost:8000/redirect -H "Content-Type: application/json" -d '{"query": "Тема письма"}'
```

## Требования

- Python 3.10+
- FastAPI
- LangChain
- GigaChat
- FAISS
- SentenceTransformerEmbeddings
- JIRA
- smtplib

## Автор

Автор проекта — Senior Python Developer.