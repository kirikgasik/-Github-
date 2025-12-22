import time
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

n = 10_000_000
data = list(range(n))
target = -1  
print(f"Поиск в списке из {n} элементов...")

start_linear = time.time()
found_linear = target in data
end_linear = time.time()
time_linear = end_linear - start_linear
print(f"Линейный поиск (O(n)): {time_linear:.6f} сек.")

start_binary = time.time()
found_binary = binary_search(data, target)
end_binary = time.time()
time_binary = end_binary - start_binary
print(f"Бинарный поиск (O(log n)): {time_binary:.6f} сек.")

if time_binary > 0:
    speedup = time_linear / time_binary
    print(f"\nРезультат: Бинарный поиск быстрее линейного примерно в {int(speedup):,} раз!")
