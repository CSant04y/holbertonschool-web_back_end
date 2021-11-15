#!/usr/bin/env python3
"""Returns bytes from password fed in
"""
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from db import DB
from user import User


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
            self._db.find_user_by('email')
        except NoResultFound:
            new_register = self._db.add_user(email, _hash_password(password))
            return new_register
        else:
            raise ValueError(f'User {email} already exists')


def _hash_password(password: str) -> bytes:
    """Returns a Hashed password
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
