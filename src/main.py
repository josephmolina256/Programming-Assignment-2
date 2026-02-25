from .policies import LRU, OPTFF, FIFO

# sample input and capacity for testing
sample_input = [1, 2, 3, 2, 1, 4, 5, 1]
sample_capacity = 3

"""correct output:
FIFO: 2 hits, 6 misses
LRU: 3 hits, 5 misses
"""

def main():
    capacity = sample_capacity
    requests = sample_input
    m = len(requests)

    fifo_cache = FIFO(capacity)
    lru_cache = LRU(capacity)
    optff_cache = OPTFF(capacity)

    lru_hits = fifo_hits = optff_hits = 0
    for item in requests:
        if fifo_cache.request(item):
            fifo_hits += 1
        if lru_cache.request(item):
            lru_hits += 1
        if optff_cache.request(item):
            optff_hits += 1

    print(f"FIFO: {fifo_hits} hits, {m - fifo_hits} misses")
    print(f"LRU: {lru_hits} hits, {m - lru_hits} misses")
    print(f"OPTFF: {optff_hits} hits, {m - optff_hits} misses")
    
    return 0


if __name__ == "__main__":
    main()