#!/usr/bin/env python3
"""write a redis class that interacts with redis"""


import redis
from typing import Any
import uuid


class Cache:
    """a cache class that interacts with redis"""
    def __init__(self) -> None:
        """ the constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """store data into redis db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return(key)
