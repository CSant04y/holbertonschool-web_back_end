#!/usr/bin/env python3.7
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

asyncio.run(wait_n(5, 5))
asyncio.run(wait_n(10, 7))
asyncio.run(wait_n(10, 0))
