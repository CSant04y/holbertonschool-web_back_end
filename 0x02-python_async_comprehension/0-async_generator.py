#!/usr/bin/env python3.7
"""[coroutine called async_generator that takes no arguments]
"""


import random
import asyncio


async def async_generator():
    """[This is an async generator that loops ten times]
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
