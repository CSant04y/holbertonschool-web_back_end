#!/usr/bin/env python3
""" This Class inherits from BasicAuth
"""

from api.v1.auth.auth import Auth
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
