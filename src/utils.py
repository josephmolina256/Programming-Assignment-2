def read_requests(path: str):
	"""
	Reads input file from path.
	Returns:
		k: capacity of cache
		m: number of requests
        requests: list of requests
	"""
	with open(path, "r") as f:
		lines = [line.strip() for line in f if line.strip()]
	
	if not lines:
		raise ValueError("Empty input file")

	if len(lines) != 2:
		raise ValueError("Malformed input. Wrong number of lines")

	first_line = lines[0].split()
	if len(first_line) != 2:
		raise ValueError("Malformed input. First line must contain k and m")

	k = int(first_line[0])
	m = int(first_line[1])

	if k < 1:
		raise ValueError("Malformed input. k must be at least 1")

	requests = [int(x) for x in lines[1].split()]

	if len(requests) != m:
		raise ValueError("Malformed input. Wrong number of requests")

	return k, m, requests

def write_output(fifo_misses, lru_misses, optff_misses, output_path="data/example.out"):
	"""
	Writes to output file.
	"""
	with open(output_path, "w") as f:
		f.write(f"FIFO  : {fifo_misses}\n")
		f.write(f"LRU   : {lru_misses}\n")
		f.write(f"OPTFF : {optff_misses}\n")

def write_error(output_path, message):
	"""
	Writes an error to output file for malformed inputs.
	"""
	with open(output_path, "w") as f:
		f.write(message)