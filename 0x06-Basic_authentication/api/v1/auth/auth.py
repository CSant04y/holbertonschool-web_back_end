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
        return False

    def authorization_header(self, request=None) -> str:
        """
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns flask Request object
        """
        return request
