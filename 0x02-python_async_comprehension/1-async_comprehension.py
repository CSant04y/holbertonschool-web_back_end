#!/usr/bin/env python3.7
'''

'''


import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """[This function collects list of numbers and returns them]

    Returns:
        typing.List[float]: [List of floats]
    """
    result_list = [num async for num in async_generator()]
    return result_list
