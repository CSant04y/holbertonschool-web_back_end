#!/usr/bin/env python3.7
"""[coroutine called async_generator that takes no arguments]
"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """[This is an async generator that loops ten times]
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
