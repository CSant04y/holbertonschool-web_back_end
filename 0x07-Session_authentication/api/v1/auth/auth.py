#!/usr/bin/env python3
"""Class that manages API Authentication
"""
from flask import request
from os import getenv
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
        '''Checks to see if any of excluded path end in *'''
        wildcard = any(rex.endswith("*") for rex in excluded_paths)

        if not wildcard:
            if path in excluded_paths:
                return False

        for rex in excluded_paths:
            if rex[-1] == '*':
                if path.startswith(rex[:-1]):
                    return False
            if rex == path:
                return False
        return True

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

    def session_cookie(self, request=None):
        """[This returns a cookie value on request]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
        if not request:
            return None

        cookie_name = getenv("SESSION_NAME")

        return request.cookies.get(cookie_name)
