""" It handle user data """

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .jwttoken import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """Finds the user which generated the token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="The Credential Could Not Be Validated",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token, credentials_exception)
