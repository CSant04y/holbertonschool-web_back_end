#!/usr/bin/env python3
"""[Simple Pagenation]
"""


import csv
import math
from typing import Tuple
from typing import List
from typing import Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """[This method gets page]

        Args:
            page (int, optional): [page that is passed]. Defaults to 1.
            page_size (int, optional): [page size]. Defaults to 10.

        Returns:
            List[List]: [returns list of list]
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """[returns dictonary]

        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            Dict[str, any]: [description]
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < page_size else None
        prev_page = page - 1 if page > 1 else None

        dataDict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return dataDict
