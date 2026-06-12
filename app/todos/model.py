from database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,String,Enum,DateTime,ForeignKey
from schema import Priority,Status
from auth.model import User


class Todos(Base):
    __tablename__="todos"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(200),nullable=False)
    shortDescription: Mapped[str] = mapped_column(String(300),nullable=False)
    priority: Mapped[Enum] = mapped_column(Enum(Priority))
    deadLine: Mapped[DateTime] = mapped_column(DateTime,nullable=False)
    usersId: Mapped[int] = mapped_column(ForeignKey("users.id")) 
    auther: Mapped[User] = relationship(back_populates="todos")
    status: Mapped[Enum] = mapped_column(Enum(Status))

