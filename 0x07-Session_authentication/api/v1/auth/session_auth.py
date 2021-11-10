#!/usr/bin/env python3
""" Class SessionAuth that inherits from Auth
"""


from api.v1.auth.auth import Auth
from uuid import uuid4
from os import getenv
from models.user import User


class SessionAuth(Auth):
    """[This class is the basis of Session authentication]

    Args:
        Auth ([Class]): [Class that is being inhertited]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[This method creates a session for authentication]

        Args:
            user_id (str): [This is the Session ID]. Defaults to None.

        Returns:
            str: [description]
        """
        if not user_id or not isinstance(user_id, str):
            return None

        else:
            sessionID = str(uuid4())
            self.user_id_by_session_id[sessionID] = user_id
            return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[This gets the user id and gets the session ID ]

        Args:
            session_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [User ID]
        """

        if not session_id or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        session_cookie = self.session_cookie(request)
        session_id = self.user_id_for_session_id(session_cookie)
        return User.get(session_id)

    def destroy_session(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        session_cookie = self.session_cookie(request)
        if not request:
            return False
        elif not session_cookie:
            return False

        user_id = self.user_id_for_session_id(session_cookie)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(session_cookie)
        return True
