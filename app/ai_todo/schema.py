from pydantic import BaseModel
from auth.schema import user

class AITodoDaily(BaseModel):
    id :int 
    users: user = None
    Date : str
    AiContent: str


class AITodoWeekly(BaseModel):
    id: int
    userId: int
    Date: str
    AiContent: str