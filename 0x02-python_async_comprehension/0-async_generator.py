#!/usr/bin/env python3
"""
Async Generator Module

Defines an asynchronous generator coroutine that:
- Loops 10 times
- Waits 1 second between iterations asynchronously
- Yields a random float between 0 and 10 using the random module
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine async_generator
    yield random number 0-10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

