from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from schema import SignIn,SignUp,ResetPassword,ForgotPassword
from database import get_db


auth_router = APIRouter()


@auth_router.get("/me")
def me():
    return {
        "message": "user profile fetched successfully"
    }

@auth_router.post("/sign-in")
async def sigin(body: SignIn,db: Session = Depends(get_db)):
    token = "hgjkl"
    return{
        "message": "sign-in succesfully",
        "access_token": token
    }


@auth_router.post("/sign-up")
async def singup(body:SignUp,db: Session = Depends(get_db)):
    user = {}
    return{
        "message":"Sign up succesfully",
        "user": user
    }


@auth_router.post("/sign-out",)
async def signout(db: Session = Depends(get_db)):
    return {
        "message":"Sign out succesfully"
    }

@auth_router.post("/reset-password")
async def reset_password(body:ResetPassword,db: Session = Depends(get_db)):
    return{
        "message":"Your password has beem reseted succesfully"
    }

@auth_router.post("/forgot-passowrd-link")
async def forgot_password_link(body: ForgotPassword,db: Session = Depends(get_db)):
    return{
        "message":"Reset-Link send successfully"
    }

@auth_router.post("/reset-password-forgot")
async def reset_password_forgot(db: Session = Depends(get_db)):
    return {
        "message":"Your password has been reseted! Please login again"
    }