""" Function for hashing methods """
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """Hash Class"""

    @staticmethod
    def bcrypt(password: str):
        """Responsible for hashing the password"""
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed, normal):
        """Responsible for checking if the password matches"""
        return pwd_cxt.verify(normal, hashed)
