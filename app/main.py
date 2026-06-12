from fastapi import FastAPI
from api import authenticated_api_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


app.include_router(authenticated_api_router, prefix="", tags=["Root"])
@app.get("/")
def health():
    return {
        "message":"Fastapi is working fine"
    }
