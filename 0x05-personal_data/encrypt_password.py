#!/usr/bin/env python3
"""
Hashes password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """[Hashes password]

    Args:
        password (str): [password to be hashed]

    Returns:
        bytes: [return]
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """[validates hashed passwd]

    Args:
        hashed_password (bytes): [description]
        password (str): [description]

    Returns:
        bool: [description]
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
