from pydantic import BaseModel
import enum
from auth.schema import user

class Priority(enum):
    LOW ="low"
    MEDIUM="medium"
    HIGH= "high"
    CRICTAL = "circtal"
    

class Status(enum):
    STARTED="started"
    IN_PROGRESS ="in_progress"
    COMPLETED = "completed"

class Todo(BaseModel):
    id: int
    name: str
    shortDescription: str
    priority: Priority
    deadLine: str
    users : user = None
    status: Status
