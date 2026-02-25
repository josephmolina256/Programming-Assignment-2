from collections import deque

class FIFO:
    """First in first out implementation
    with O(m) runtime and O(k) space 
    where k is the capacity of our cache 
    and m is the number of requests.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.queue = deque()

    def request(self, item):
        if item in self.cache:
            return True  # hit
        
        # miss
        if len(self.cache) == self.capacity:
            oldest = self.queue.popleft()
            self.cache.remove(oldest)

        self.cache.add(item)
        self.queue.append(item)
        return False 
        
