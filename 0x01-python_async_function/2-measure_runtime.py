#!/usr/bin/env python3
"""Measure the average runtime of wait_n function"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per coroutine call.

    Args:
        n (int): number of times to run wait_random concurrently
        max_delay (int): maximum delay allowed for wait_random

    Returns:
        float: average time per call
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
