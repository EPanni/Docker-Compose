""" This module contains the models used in the request"""
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    """ User Model """
    username: str
    company: str
    password: str
    
    class Config:
        orm_mode=True


class Login(BaseModel):
    """ Login Model """
    username: str
    password: str

    class Config:
        orm_mode=True


class Token(BaseModel):
    """ Token Model """
    access_token: str
    token_type: str
    
    class Config:
        orm_mode=True


class TokenData(BaseModel):
    """ Token Data Model """
    username: Optional[str] = None
    
    class Config:
        orm_mode=True
