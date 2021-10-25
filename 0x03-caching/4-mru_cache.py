#!/usr/bin/env python3
"""[Least Recently Used]
"""


from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """[This is the Least Recently Used Caching class]

    Args:
        BaseCaching ([Parent Class]): [This is the class that LRUcache]
    """

    def __init__(self) -> None:
        """[Initilization using parent init]
        """
        super().__init__()
        self.mru_dict = OrderedDict()

    def put(self, key, item):
        """[This assigns the dictonary]
        Args:
            key ([str]): [key]
            item ([str]): [Value]
        """
        if not key or not item:
            return

        self.mru_dict[key] = item
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.mru_dict))
            del self.cache_data[discarded]
            print("DISCARD: {}".format(discarded))

        self.mru_dict.move_to_end(key, last=False)

    def get(self, key):
        """[Returns value based of key]

        Args:
            key ([str]): [key]
        """
        if key in self.cache_data:
            self.mru_dict.move_to_end(key, False)
            return self.cache_data[key]

        return None
