import time
class Timer:
    def __init__(self, name="Операция", verbose=True):
        self.name = name
        self.verbose = verbose
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if self.verbose:
            print(f"{self.name}: {self.elapsed_time:.4f} сек")
        return False
    def get_elapsed_time(self):
        return self.elapsed_time if self.elapsed_time is not None else 0
print()
with Timer("Внешний блок"):
    time.sleep(0.5)
    with Timer("Внутренний блок 1"):
        time.sleep(0.3)
    with Timer("Внутренний блок 2"):
        time.sleep(0.2)