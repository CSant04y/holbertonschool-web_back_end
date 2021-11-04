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
