import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {duration:.4f} сек")
        return result
    return wrapper
@timer
def slow_func(n):
    total = 0
    for i in range(n):
        total += i
    return total
result = slow_func(10000000)
print(f"Результат: {result}")