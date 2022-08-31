from curses import echo
from lib2to3.pytree import Base
from os import environ
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

#TODO: Replace it to use .env
url = ("User:Password@172.0.0.2/DB")

engine = create_engine(f"postgresql://{url}", echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
