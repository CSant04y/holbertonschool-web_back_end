#!/usr/bin/env python3
"""Returns bytes from password fed in
"""
from flask.globals import request
from sqlalchemy.orm import session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.functions import user
from werkzeug.exceptions import abort
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

    def create_session(self, email: str) -> str:
        """This creates a session"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> user:
        """[This gets user form session_id]

        Args:
            session_id (str): [This is the id of the session]

        Returns:
            user: [if found]
        """

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """This updates the sorrespoding user id to None"""
        if user_id:
            self._db.update_user(user_id, session_id=None)

        return None

    def get_reset_password_token(self, email: str) -> str:
        """[This takes in email argument and returns a token]
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=_generate_uuid())
            return user.reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """This updates the password for the user"""
        if not reset_token:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
            pwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=pwd,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """Returns a Hashed password
    """

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """This generates a uuid and is returned as a str"""
    return str(uuid.uuid4())
