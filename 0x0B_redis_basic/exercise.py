#!/usr/bin/env python3
"""
This writes strings to redis
"""
import redis
import uuid
from typing import Callable, Union, Optional
from functools import wraps

UnionTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """counts the number of times a method is called"""
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """Wraper func for count_calls"""
        self._redis.incr(method.__qualname__)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """This gets the call history"""
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwrgs):
        self._redis.rpush(inputs, str(args))
        returned_method = method(self, *args, **kwrgs)
        self._redis.rpush(outputs, str(returned_method))
        return returned_method
    return wrapper


class Cache:
    """[This is the Cahcing class with methods for caching]
    """

    def __init__(self):
        """Instantiates class obj"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
