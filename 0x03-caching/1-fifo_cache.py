#!/usr/bin/env python3
"""[FIFO caching with inhertince from BaceCaching]
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """[Class FIFO Cache, FIRST IN FIRST OUT]

    Args:
        BaseCaching ([Parent Class]): [This is the parent class]
    """

    def __init__(self):
        '''Instantation of class attributes'''
        super().__init__()
        self.key_indcies = []

    def put(self, key, item):
        """[This assigns the dictionary self.cache_data
            the item value for the key]

        Args:
            key ([string]): [key to dictonary]
            item ([string]): [value of key]
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.key_indcies.pop(0)

                del self.cache_data[discarded_key]

                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.key_indcies.append(key)

    def get(self, key):
        """[This gets value based of key]

        Args:
            key ([string]): [Key value for dictonary]
        """
        if key is None or not key:
            return None

        else:
            return self.cache[key]
