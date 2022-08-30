from ast import Str
from sqlalchemy import Column, Integer, String, Text
from database.database import Base

class UserMod(Base):
    __tablename__ = "Users"
    Id = Column(Integer, primary_key=True)
    username = Column(String(255))
    company = Column(String(255))
    password = Column(Text)
