#!/usr/bin/env python3
"""
Async Comprehensions Module

Defines a coroutine that collects 10 random numbers
from an asynchronous generator using async comprehensions.
"""

from typing import List

Vector = List[float]
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """
    Asynchronous coroutine that collects 10 random float numbers
    from an async generator using an async comprehension.

    Returns:
        Vector: A list of 10 random float numbers between 0 and 10.
    """
    return [y async for y in async_generator()]

