#!/usr/bin/env python3
"""
Runtime for Parallel Comprehensions Module

Defines a coroutine that measures the total execution time
of running async_comprehension concurrently four times.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous coroutine that measures the total runtime of
    executing async_comprehension concurrently 4 times using asyncio.gather.

    Returns:
        float: The total elapsed time in seconds.
    """
    begin = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()
    return end - begin

