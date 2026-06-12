# AI Todo Master App

A FastAPI backend for managing todos with authentication, regular todo workflows, AI-assisted todo summaries, and SQLAlchemy-based database models.

The application is organized into focused modules for auth, todos, and AI todo features, making it easier to build, extend, and maintain each part of the system independently.

## Features

- FastAPI application entry point
- Modular API routing
- Auth route namespace
- Todo route namespace
- AI todo route namespace
- SQLAlchemy database setup scaffold
- Initial `User` and `Todos` model files
- Python 3.12 project managed with `uv`

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn through `fastapi[standard]`
- SQLAlchemy
- `uv` for dependency and virtual environment management

## Project Structure

```text
todo-master-ai-app/
├── app/
│   ├── main.py              # FastAPI app instance and root health route
│   ├── api.py               # Central API router composition
│   ├── config.py            # Configuration placeholder
│   ├── database.py          # SQLAlchemy engine, session, and Base setup
│   ├── auth/
│   │   ├── router.py        # Auth endpoints
│   │   ├── schema.py        # Auth Pydantic schemas
│   │   ├── model.py         # User SQLAlchemy model
│   │   └── services.py      # Auth service logic placeholder
│   ├── todos/
│   │   ├── router.py        # Todo endpoints
│   │   ├── schema.py        # Todo Pydantic schemas and enums
│   │   ├── model.py         # Todos SQLAlchemy model
│   │   └── services.py      # Todo service logic placeholder
│   └── ai_todo/
│       ├── router.py        # AI todo endpoints
│       ├── schema.py        # AI todo schemas placeholder
│       ├── model.py         # AI todo models placeholder
│       └── services.py      # AI todo service logic placeholder
├── pyproject.toml
├── uv.lock
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12
- `uv`

Install `uv` if you do not already have it:

```bash
pip install uv
```

### Install Dependencies

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root before running the application with database support:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/todo_master
```

For production, keep this value in your hosting provider's secret/environment variable system instead of committing it to Git.

### Run The Application

Because the imports are currently written relative to the `app` directory, run the server from inside `app`:

```bash
cd app
uv run fastapi dev main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API docs:

```text
http://127.0.0.1:8000/docs
```

