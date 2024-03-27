#!/usr/bin/env python3
"""module declare redis class and method"""

import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)

def count_calls(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper

def replay(fn):
    func_name = fn.__qualname__
    cache = redis.Redis()
    call_count = int(cache.get(func_name) or 0)
    print(f"{func_name} was called {call_count} times:")
    inputs = cache.lrange(f"{func_name}:inputs", 0, -1)
    outputs = cache.lrange(f"{func_name}:outputs", 0, -1)
    for inp, outp in zip(inputs, outputs):
        print(f"{func_name}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")

if __name__ == "__main__":
    cache = Cache()

    # Writing strings to Redis
    data = b"hello"
    key = cache.store(data)
    print(key)

    # Reading from Redis and recovering original type
    print(cache.get(key))  # Bytes
    print(cache.get_str(key))  # String

    # Incrementing values
    @count_calls
    def increment_value(value):
        return value

    for i in range(5):
        increment_value(i)

    print(cache.get(increment_value.__qualname__))  # 5

    # Storing lists
    @call_history
    def add_numbers(a, b):
        return a + b

    add_numbers(2, 3)
    add_numbers(4, 5)
    add_numbers(6, 7)

    # Retrieving lists
    replay(add_numbers)
