#!/usr/bin/env python3.7
'''
An async routine that takes in two ints
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[this executes multiple coroutines at the smae time]

    Args:
        n (int): [number of times wait_random should be spawned]
        max_delay (int): [with the specified max_delay]

    Returns:
        List[float]: [List of floats in acending order]
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
