#!/usr/bin/env python3
"""Class that manages API Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This takes care of the path and returns a bool
        """
        if not path or not excluded_paths:
            return True

        if path[-1] != "/":
            path += '/'

        if path not in excluded_paths:
            return True

        if path in excluded_paths:
            return False

        return False

    def authorization_header(self, request=None) -> str:
        """This is Authorization header
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns flask Request object
        """
        return None
