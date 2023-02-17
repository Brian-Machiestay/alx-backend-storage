#!/usr/bin/env python3
"""some tests"""

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

print(cache.store("eat"))
print(cache.store("sleep"))
print(cache.store(30))
replay(cache.store)
