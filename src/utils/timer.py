import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self  # optional, in case you want to use `as` to access elapsed time inside the block

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.6f} seconds")
