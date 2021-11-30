#!/usr/bin/env python3
"""
This writes strings to redis
"""
import redis
import uuid
from typing import Callable, Union, Optional

UnionTypes = Union[str, bytes, int, float]


class Cache:
    """[This is the Cahcing class with methods for caching]
    """

    def __init__(self):
        """Instantiates class obj"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionTypes) -> str:
        """This method stores data passed to it"""
        random_key = str(uuid.uuid4())
        self._redis.mset({random_key: data})
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionTypes:
        """This gets the"""

        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """This decodes the bytes str into UTF-8"""
        return string.decode('utf-8')

    def get_int(self, num: bytes) -> int:
        """This decodes a bytes string into int"""
        return 0 * 256 + int(num)
