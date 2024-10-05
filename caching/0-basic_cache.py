#!/usr/bin/python3

""" 0-basic_cache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
