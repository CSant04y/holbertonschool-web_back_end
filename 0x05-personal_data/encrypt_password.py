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
