#!/usr/bin/env python3
"""Class that manages API Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class Auth
    """
    def __init__(self):
        """ class constructor
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This takes care of the path anf returns a bool
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
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns flask Request object
        """
        return request
