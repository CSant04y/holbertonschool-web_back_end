#!/usr/bin/env python3
"""[Least Recently Used]
"""


from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """[This is the Least Recently Used Caching class]

    Args:
        BaseCaching ([Parent Class]): [This is the class that LRUcache]
    """

    def __init__(self) -> None:
        """[Initilization using parent init]
        """
        super().__init__()
        self.lru_dict = OrderedDict()

    def put(self, key, item):
        """[This assigns the dictonary]
        Args:
            key ([str]): [key]
            item ([str]): [Value]
        """
        if key and item:
            self.lru_dict[key] = item
            self.lru_dict.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.lru_dict))
            del self.cache_data[discarded]
            print("DISCARD: {}".format(discarded))

        if len(self.lru_dict) > BaseCaching.MAX_ITEMS:
            self.lru_dict.popitem(last=False)

    def get(self, key):
        """[Returns value based of key]

        Args:
            key ([str]): [key]
        """
        if key in self.cache_data:
            self.lru_dict.move_to_end(key)
            return self.cache_data[key]

        return None
