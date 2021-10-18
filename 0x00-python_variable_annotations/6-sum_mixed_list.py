#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes a 
list mxd_lst of integers and floats and returns their sum as a float
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns sum of list to float'''
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum
