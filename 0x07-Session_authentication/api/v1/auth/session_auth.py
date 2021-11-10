#!/usr/bin/env python3
""" Class SessionAuth that inherits from Auth
"""


from api.v1.auth.auth import Auth
from uuid import uuid4


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
            self.user_id_by_session_id[str(uuid4())] = user_id
            return self.user_id_by_session_id
