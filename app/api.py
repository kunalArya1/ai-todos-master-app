from fastapi import APIRouter

from auth.router import auth_router
from todos.router import todo_router
from ai_todo.router import ai_todo_router


authenticated_api_router = APIRouter()


authenticated_api_router.include_router(auth_router,prefix="/auth",tags=["auth"])
authenticated_api_router.include_router(todo_router,prefix="/todos",tags=["Todo"])
authenticated_api_router.include_router(ai_todo_router,prefix="/ai/todo",tags=["AI_Todos"])
