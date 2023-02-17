#!/usr/bin/env python3
"""write a redis class that interacts with redis"""


import redis
from typing import Any, Union, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """a decorator function that counts calls to Cache"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """the wrapper class"""
        args[0]._redis.incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


class Cache:
    """a cache class that interacts with redis"""
    def __init__(self) -> None:
        """ the constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, float, bytes]) -> str:
        """store data into redis db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return(key)

    def get(self, key: str, fn: Callable = None) -> Any:
        """convert a value to a custom type"""
        val = self._redis.get(key)
        if fn is None:
            return(val)
        val = fn(val)
        return val

    def get_str(self) -> Callable:
        """return the conversion function for a string"""
        return lambda x: str(x)

    def get_int(self) -> Callable:
        """return the conversion function for an int"""
        return lambda x: int(x)
