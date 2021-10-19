#!/usr/bin/env python3.7
"""[Measures the runtime of imported function]
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[This measures the execution time for wait_n function]

    Args:
        n (int): [description]
        max_delay (int): [total_time / n]

    Returns:
        float: [time it took]
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    return (end_time - start_time) / n
