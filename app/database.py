from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os 


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(autoflush=True,autocommit=True,bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()

    finally:
        db.close()
