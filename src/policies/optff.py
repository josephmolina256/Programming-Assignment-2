class OPTFF:
    """Optimal future-free needs implementation 
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()

    def request(self, item):
        if item in self.cache:
            return True  # hit
        
        # miss
        if len(self.cache) == self.capacity:
            pass

        return False 
        
