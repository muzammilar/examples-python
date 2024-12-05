# app/math_util.py

from time import time

# LRU cache implementation

class StorageObject:
    def __init__(self, value, timestamp):
        self.timestamp = timestamp
        self.value = value

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # lru map

    # get: return a value if there's a key, else return a None
    def get(self, key):
        if key in self.cache:
            return self._update_timestamp_and_return(key)
        return None

    # write: takes a key and a value and adds it to the cache
    def write(self, key, value):
        if key not in self.cache:
            self._remove_oldest()
        self.cache[key] = StorageObject(value, time())

    def _update_timestamp_and_return(self, key):
        self.cache[key].timestamp = time()
        return self.cache[key].value

    def _remove_oldest(self):
        if len(self.cache) >= self.capacity:
            oldest_key = min(self.cache, key=lambda k: self.cache[k].timestamp)
            del self.cache[oldest_key]
