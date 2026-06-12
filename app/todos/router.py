from fastapi import APIRouter

todo_router = APIRouter()


@todo_router.get("/")
def get_all_todos():
    return {
        "message":"All todo fetched succesfully"
    }

@todo_router.get("/todos")
def get_todos():
    db_todos = {}
    return{
        "message":"All todos fetched succesfully",
        "todos": db_todos
    }

@todo_router.get("/todo/{id}")
async def get_todo_by_id():
    db_todo = {}
    return{
        "message":"Todo fetched succesfully",
        "todo": db_todo
    }


@todo_router.post("/todos")
async def create_todo():
    return{
        "message":"Todo added successfully"
    }

@todo_router.put("/todos")
async def update_todo():
    return {
        "message":"Todo updated succesfully"
    }

@todo_router.delete("/todos")
async def delete_todo():
    return{
        "message":"Todo deleated succesfully"
    }

@todo_router.post("/todos/staus")
async def update_status():
    return{
        "message":"Todo status updated succesfully"
    }

