#!/usr/bin/env python3
""" This Class inherits from BasicAuth
"""

from api.v1.auth.auth import Auth
from models.user import User
from models.base import Base
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """Class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[extracts a base64 encoded str from str]

        Args:
            authorization_header (str): [Header authorization for API]

        Returns:
            str: [base64 encoded str]
        """
        if not authorization_header or not isinstance(authorization_header,
                                                      str):
            return None

        if authorization_header.startswith("Basic "):
            return authorization_header[6:]
        # base64.b64encode(authorization_header[6:].encode("ascii"))

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """[Decodes base64 str]

        Args:
            base64_authorization_header (str): [API request header]

        Returns:
            str: [decoded str]
        """
        if not base64_authorization_header or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            base = base64.b64decode(encoded)
            return base.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """[summary]

        Args:
            self ([type]): [description]
            str ([type]): [description]
        """
        if not decoded_base64_authorization_header or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        elif ":" not in decoded_base64_authorization_header:
            return None, None

        base = decoded_base64_authorization_header.split(':', 1)

        return base[0], base[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """[returns User Instance based of username and password]

        Args:
            self ([type]): [description]
        """

        if not user_email or not isinstance(user_email, str):
            return None

        elif not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})

        except BaseException:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[Overloads Auth]
        """
        auth_header = self.authorization_header(request)
        base64_str = self.extract_base64_authorization_header(auth_header)
        decoded_str = self.decode_base64_authorization_header(base64_str)
        credentials = self.extract_user_credentials(decoded_str)
        user = self.user_object_from_credentials(
            credentials[0], credentials[1])
        return user
