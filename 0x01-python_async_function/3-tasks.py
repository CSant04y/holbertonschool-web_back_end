#!/usr/bin/env python3.7
"""[Function that returns asyncio.task]
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[summary]

    Args:
        max_delay (int): [description]

    Returns:
        asyncio.Task: [description]
    """
    return asyncio.Task(wait_random(max_delay))
