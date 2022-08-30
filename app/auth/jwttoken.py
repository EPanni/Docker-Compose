""" Modules responsible for handling related to the jwt token"""
from base64 import encode
from datetime import datetime, timedelta
from os import environ
from jose import JWTError, jwt
from models.schemas import TokenData

SECRET_KEY = environ.get("SECRET_KEY")
ALGORITHM = environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict):
    "Creates an access token with expires after a certain time"
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_token(token: str, credentials_exception):
    """Finds the user which generated the token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except:
        raise credentials_exception
