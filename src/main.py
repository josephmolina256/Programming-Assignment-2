import sys
from .policies import LRU, OPTFF, FIFO
from .utils import read_requests, write_output, write_error

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("""Usage:
        python -m src.main <input file path>
        python -m src.main <input file path> <output file path>""")
        return 1

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) == 3 else None

    try:
        k, m, requests = read_requests(input_path)
    except:
        if output_path is not None:
            write_error(output_path, "INVALID INPUT")
        else:
            print("INVALID INPUT")
        return 1

    fifo = FIFO(k)
    lru = LRU(k)
    optff = OPTFF(k, requests)

    fifo_misses = 0
    lru_misses = 0
    optff_misses = 0

    for request in requests:
        if not fifo.request(request):
            fifo_misses += 1
        if not lru.request(request):
            lru_misses += 1
        if not optff.request(request):
            optff_misses += 1

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")

    if output_path is not None:
        write_output(fifo_misses, lru_misses, optff_misses, output_path)

    return 0

if __name__ == "__main__":
    main()