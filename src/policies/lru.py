class LRU:
    """Least recently used implementation 
    with O(mk) runtime  and O(k) space 
    where k is the capacity of our cache 
    and m is the number of requests.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.last_used = {} # key: item, value: last access time
        self.time = 0

    def request(self, item):
        self.time += 1
        if item in self.cache:
            self.last_used[item] = self.time  # update item's time
            return True  # hit
        
        # miss
        if len(self.cache) == self.capacity:
            # find the lru item
            oldest = min(self.last_used, key=self.last_used.get)
            self.cache.remove(oldest)
            del self.last_used[oldest]

        self.cache.add(item)
        self.last_used[item] = self.time  # update item's time
        return False 
        
