#!/usr/bin/env python3
"""This shows the function with the correct duck type
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns anything'''
    if lst:
        return lst[0]
    else:
        return None
