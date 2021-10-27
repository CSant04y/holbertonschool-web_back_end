#!/usr/bin/env python3
"""[Simple helper function that returns a tuple]
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[This function takes in two int args]

    Args:
        page (int): [The page number passed]
        page_size (int): [How many items per page]

    Returns:
        Tuple[int, int]: [description]
    """
    endIndex = page_size * page

    return (endIndex - page_size, endIndex)
