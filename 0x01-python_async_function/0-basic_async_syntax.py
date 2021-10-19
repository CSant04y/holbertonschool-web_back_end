#!/usr/bin/env python3.7
"""
 asynchronous coroutine that takes in an integer argument
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[This function is a asynchronous co-routine]

    Args:
        max_delay (int, optional): [is seconds in delay]. Defaults to 10.

    Returns:
        float: [number of seconds that it takes]
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return float(wait_time)
