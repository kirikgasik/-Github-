import time
import random
def find_duplicates(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates
sizes = [5000, 10000]
results = []
print("Начинаем замеры... (это может занять несколько секунд)")
for size in sizes:
    test_list = [random.randint(1, size) for _ in range(size)]
    start_time = time.time()
    find_duplicates(test_list)
    end_time = time.time()
    duration = end_time - start_time
    results.append(duration)
    print(f"Размер списка: {size} | Время выполнения: {duration:.4f} сек.")
ratio = results[1] / results[0]
print("-" * 30)
print(f"При увеличении данных в 2 раза, время выросло примерно в {ratio:.2f} раз.")
print("Вывод: Для алгоритмов O(n²) рост данных в N раз приводит к росту времени в N² раз.")
print("В данном случае: 2² = 4. Время должно увеличиться примерно в 4 раза.")