#!/usr/bin/env python3
""" Async python first tasks
    takes an int representing the time of delay and return it

    """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Main function of the task
    Asynchronous coroutine
    max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
~               
