#!/usr/bin/env python3.7
"""[getting runtime for four parallel comprehensions]
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[This measures the runtime of executing four
     calls to async_comprehansion]

    Returns:
        float: [total_runtime]
    """
    t1 = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    t2 = time.perf_counter()

    return t2 - t1
