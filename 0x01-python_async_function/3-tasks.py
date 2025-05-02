#!/usr/bin/env python3
"""Fourth async task: Returns an asyncio.Task object"""


import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio Task for wait_random.

    Args:
        max_delay (int): maximum delay passed to wait_random

    Returns:
        asyncio.Task: a Task object wrapping wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
