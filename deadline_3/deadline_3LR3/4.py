import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def tail_fibonacci(n, a=0, b=1):
    if n == 0: return a
    if n == 1: return b
    return tail_fibonacci(n - 1, b, a + b)
n = 35
print(f"Factorial(5): {fibonacci(5)} | Tail: {tail_fibonacci(5)}")