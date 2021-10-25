#!/usr/bin/env python3
"""[This is LIFO Caching]
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """[LIFO Caching class that inherits from BaseCaching]

    Args:
        BaseCaching ([Class Parent]): [Class that is being inhertited from]
    """

    def __init__(self):
        '''This class instantiates'''
        super().__init__()
        self.key_indcies = []

    def put(self, key, item):
        """[This Method assigns key to item]

        Args:
            key ([str]): [Key]
            item ([str]): [value]
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
                self.key_indcies.remove(key)

            if len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[self.key_indcies[self.MAX_ITEMS - 1]]
                discarded_key = self.key_indcies.pop(self.MAX_ITEMS - 1)
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.key_indcies.append(key)

    def get(self, key):
        """[This gets value based of key]

        Args:
            key ([string]): [Key value for dictonary]
        """
        if key:
            return self.cache_data[key]

        else:
            return None
