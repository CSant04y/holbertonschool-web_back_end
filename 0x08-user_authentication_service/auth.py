#!/usr/bin/env python3
"""Returns bytes from password fed in
"""
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from db import DB
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ This method registers a user using their email
            and their password
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            new_register = self._db.add_user(email, _hash_password(password))
            return new_register
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        '''This checks to make sure that user is valid'''
        try:
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), user.hashed_password)


def _hash_password(password: str) -> bytes:
    """Returns a Hashed password
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def _generate_uuid() -> str:
    """This generates a uuid and is returned as a str"""
    return str(uuid.uuid4())
