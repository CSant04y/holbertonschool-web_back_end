#!/usr/bin/env python3
"""
annotate function that is given
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Gets elements length'''
    return [(i, len(i)) for i in lst]
