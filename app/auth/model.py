from database import Base
from pydantic import EmailStr
from sqlalchemy.orm import mapped_column,Mapped,relationship
from typing import List
from sqlalchemy import String,Enum
from schema import EmailPreferance
from todos.schema import Todo


class User(Base):
    __tablename__ = "Users"

    id : Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(40),nullable=False)
    email : Mapped[EmailStr] = mapped_column(EmailStr(200),nullable=False)
    password: Mapped[str] = mapped_column(String(20),nullable=False)
    profileImage: Mapped[str] = mapped_column(String(300),nullable=False)
    emailPreferance: Mapped[EmailPreferance] = mapped_column(Enum(EmailPreferance))
    Todos: Mapped[List["Todo"]] = relationship(back_populates="auther")
    
