#!/usr/bin/env python3
"""[Caching system that inherits from BacicCacheing]
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """[Class BasicCache in whuch a simple cache implementaion is done]

    Args:
        BaseCaching ([parent class]): [Where the data will be stored]
    """
    def put(self, key, item):
        '''This assigns key with item in dictonary'''
        if not key or not item:
            pass

        else:
            self.cache_data[key] = item

    def get(self, key):
        '''This gets the value form dictonary using key'''
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
