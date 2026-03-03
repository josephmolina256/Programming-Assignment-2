class OPTFF:
    """Optimal Farthest-in-Future implementation 
    with O(k*m^2) runtime  and O(k) space 
    where k is the capacity of our cache 
    and m is the number of requests.
    """
    def __init__(self, capacity, requests):
        self.capacity = capacity
        self.requests = requests
        self.cache = set()
        self.current_index = 0

    def request(self, item):
        i = self.current_index
        self.current_index += 1

        if item in self.cache:
            return True  # hit
        
        # miss
        if len(self.cache) == self.capacity:
            farthest_index = -1
            farthest_item = None
            # iterate through cache to find furthest item in future
            for n in self.cache:
                next_index = None
                # look ahead in requests
                for j in range(i + 1, len(self.requests)):
                    if self.requests[j] == n:
                        next_index = j
                        break
                # remove n if not used in future
                if next_index is None:
                    farthest_item = n
                    break  
                # if n is used, compare its index to furthest
                if next_index > farthest_index:
                    farthest_index = next_index
                    farthest_item = n
            self.cache.remove(farthest_item)
        self.cache.add(item)
        return False 
        
