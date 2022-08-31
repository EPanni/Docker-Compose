""" Main module"""
import sys 
import os
from os import environ
sys.path.insert(0, os.path.realpath(f"{__file__}/../"))

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
import uvicorn
from auth.oauth import get_current_user
from auth.hashing import Hash
from auth.jwttoken import create_access_token
from models.schemas import User
from models.models import UserMod
from database.database import engine, Base, SessionLocal


# DB
Base.metadata.create_all(engine)
db = SessionLocal()


# CORS
origins = environ.get("ORIGINS")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    """Index"""
    return {"data": " Home Page"}


@app.post("/register", status_code=201)
def create_user(request: User):
    "It hashes the pasword and creates the User"
    user_data = UserMod(
        username=request.username,
        company=request.company,
        password=Hash.bcrypt(request.password),
    )
    db.add(user_data)
    db.commit()
    return {"res": "created"}


@app.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends()):
    """Checks the user info and returns the acccess token"""
    user = db.query(UserMod).filter(UserMod.username == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    user_info = {"exp":"", "user": user.username, "password": user.password}
          
    data = {"sub": user_info}
    
    access_token = create_access_token(data=data)
    
    return {"access_token": access_token, "token_type": "bearer"}


if __name__ == "__main__":
    pass