from pydantic import BaseModel,EmailStr
import enum
from todos.schema import Todo

class EmailPreferance(enum):
    DAILY = "daily"
    WEEKLY = "weekly"

class user(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    profileImage: str
    shortBio: str = None
    emailPreferance: EmailPreferance = None
    Todos: Todo = None


class SignIn(BaseModel):
    email: EmailStr
    password: str

class SignInResponse(BaseModel):
    token: str

class SignUp(BaseModel):
    username: str
    email: EmailStr
    password: str
    profileImage: str
    shortBio: str = None

class SignUpResponse(BaseModel):
    username: str
    email:EmailStr
    profileImage: str
    shortBio: str = None

class ResetPassword(BaseModel):
    email: EmailStr
    oldPassword: str
    newPassword: str

class ForgotPassword(BaseModel):
    email: EmailStr

class MeResposne(BaseModel):
    username: str
    email: str
    profileImage: str
    shortBio: str
    emailPreferance: EmailPreferance = None
    Todos: Todo = None
