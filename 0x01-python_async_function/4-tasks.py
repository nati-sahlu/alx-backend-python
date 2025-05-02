#!/usr/bin/env python3
"""Fourth async task: run multiple task_wait_random and return delay times."""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random



async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently.

    Args:
        n (int): Number of times to run the task.
        max_delay (int): Maximum delay value for each task.

    Returns:
        List[float]: List of delays in the order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
