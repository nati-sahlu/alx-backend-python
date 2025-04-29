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
    Asynchronous generator that yields a random float between 0 and 10
    after waiting asynchronously for 1 second, repeated 10 times.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

