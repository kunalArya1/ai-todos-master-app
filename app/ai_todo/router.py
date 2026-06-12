from fastapi import APIRouter


ai_todo_router = APIRouter()

@ai_todo_router.get("/")
def me():
    return {
        "message":"Daily todo summery is returned"
    }

@ai_todo_router.post()
async def get_daily_todo_summary():
    return {
        "message":"Daily todo summary"
    }

@ai_todo_router.post()
async def get_weekly_todo_summary():
    return {
        "message":"Weekly todo summary"
    }