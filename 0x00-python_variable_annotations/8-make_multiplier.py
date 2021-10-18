#!/usr/bin/env python3
"""
This type-annotated function make_multiplier that takes a float multiplier
 as argument and returns a function that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns function that gets multiplier'''
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
