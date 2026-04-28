# MINI PROJECTS (FastAPI Collection)

This repository contains multiple small FastAPI projects for learning backend development, APIs, and basic database integration.

## Projects Included

1. `fastapi_TodoList`
2. `fastapi_CRUD(students)`
3. `fastapi_urlshort`
4. `fastapi_chatbot`

## Common Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-444444?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy (for DB-based projects)
- SQLite (local DB files)

---

## 1) `fastapi_TodoList`

A simple Todo CRUD API using FastAPI + SQLAlchemy + SQLite.

### Features

- Create todo items
- List all todos
- Update a todo by ID
- Delete a todo by ID
- Stores data in `todo.db`

### Endpoints

- `GET /todos` -> list all todos
- `POST /todos` -> create new todo
- `PUT /todos/{todo_id}` -> update existing todo
- `DELETE /todos/{todo_id}` -> delete todo

### Request Body (create/update)

```json
{
  "title": "Learn FastAPI",
  "is_done": false
}
```

---

## 2) `fastapi_students`

A student management API with CRUD operations by roll number using FastAPI + SQLAlchemy + SQLite.

### Features

- Add student record
- List all students
- Find student by `roll_no`
- Update student by `roll_no`
- Delete student by `roll_no`
- Stores data in `students.db`

### Endpoints

- `POST /students`
- `GET /students`
- `GET /students/roll/{roll_no}`
- `PUT /students/roll/{roll_no}`
- `DELETE /students/roll/{roll_no}`

### Request Body (create/update)

```json
{
  "name": "Alice",
  "roll_no": "A101",
  "course": "Computer Science",
  "marks": 90
}
```

---

## 3) `fastapi_urlshort`

A minimal URL shortener API that maps a generated short code to long URLs and stores them in `urls.txt`.

### Features

- Create short URL from long URL
- Redirect short URL to original long URL
- File-based storage (`urls.txt`)

### Endpoints

- `POST /shorten`
- `GET /{code}` -> redirects to original URL

### Request Body

```json
{
  "long_url": "https://example.com/some/very/long/url"
}
```

Note: The short URL currently returns with host `http://127.0.0.1:8000/{code}`.

---

## 4) `fastapi_chatbot`

A FastAPI chatbot backend connected to Google Gemini, plus a basic frontend page (`index.html`).

### Features

- `POST /chat` endpoint to send prompts and receive replies
- In-memory chat session for contextual conversation
- CORS enabled (dev-friendly)
- Static frontend UI in `index.html`

### Endpoints

- `GET /` -> health/status
- `POST /chat` -> chat with assistant

### Request Body

```json
{
  "message": "Hello, who are you?"
}
```

### Environment Variable Required

- `GEMINI_API_KEY` (in `.env`)

---

## Setup (Universal)

Run these from repository root (`miniprojectspython`):

1. Create virtual environment

```powershell
python -m venv .venv
```

2. Activate virtual environment (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies

```powershell
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv google-genai
```

If you want each app isolated, create a separate venv inside each project folder.

---

## Run Any Project

Use this pattern from repo root:

```powershell
uvicorn main:app --reload
```

Examples:

1. Todo API

```powershell
uvicorn fastapi_TodoList.main:app --reload
```

2. Students API

```powershell
uvicorn fastapi_students.main:app --reload
```

3. URL Shortener API

```powershell
uvicorn fastapi_urlshort.main:app --reload
```

4. Chatbot API

```powershell
uvicorn fastapi_chatbot.main:app --reload
```

Default local server:

- API: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

---

## Chatbot Frontend (Optional)

After running the chatbot backend, open `fastapi_chatbot/index.html` in your browser.  
It calls `http://127.0.0.1:8000/chat` directly.

---

<!-- ## Notes Before Pushing to GitHub

- Do not commit virtual environments (`venv`, `.venv`)
- Do not commit cache files (`__pycache__`, `.pyc`)
- Do not commit local DB/data files (`*.db`, `urls.txt` if you want clean state)
- Do not commit secrets (`.env`, API keys)

This repository now includes a root `.gitignore` to handle these. -->
