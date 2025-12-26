import time
import random
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

def demonstrate_performance():
    n = 10000
    arr = [random.randint(1, 100000) for _ in range(n)]
    idx1, idx2 = random.sample(range(n), 2)
    target = arr[idx1] + arr[idx2]
    print(f"Размер массива: {n}")
    print(f"Искомая сумма: {target}")
    print(f"Ожидаемая пара: ({arr[idx1]}, {arr[idx2]})")
    print()
    
    start_time = time.time()
    result_slow = find_pair_slow(arr, target)
    slow_time = time.time() - start_time
    print(f"Медленное решение:")
    print(f"  Результат: {result_slow}")
    print(f"  Время выполнения: {slow_time:.4f} секунд")
    
    start_time = time.time()
    result_fast = find_pair_fast(arr, target)
    fast_time = time.time() - start_time
    print(f"\nБыстрое решение:")
    print(f"  Результат: {result_fast}")
    print(f"  Время выполнения: {fast_time:.4f} секунд")
    print(f"\nУскорение: {slow_time/fast_time:.1f} раз")

def find_intersection_slow(arr1, arr2):
    result = []
    for x in arr1:
        if x in arr2:
            result.append(x)
    return result

def find_intersection_fast(arr1, arr2):
    set2 = set(arr2)
    result = []
    for x in arr1:
        if x in set2:
            result.append(x)
    return result

def demonstrate_intersection():
    print("\n" + "="*50)
    print("Другой пример: поиск пересечения двух массивов")
    print("="*50)
    
    arr1 = [random.randint(1, 10000) for _ in range(5000)]
    arr2 = [random.randint(1, 10000) for _ in range(5000)]
    start_time = time.time()
    result_slow = find_intersection_slow(arr1, arr2)
    slow_time = time.time() - start_time
    
    start_time = time.time()
    result_fast = find_intersection_fast(arr1, arr2)
    fast_time = time.time() - start_time
    print(f"Размеры массивов: {len(arr1)} и {len(arr2)}")
    print(f"Найдено общих элементов: {len(result_fast)}")
    print(f"Медленное решение: {slow_time:.4f} секунд")
    print(f"Быстрое решение: {fast_time:.4f} секунд")
    print(f"Ускорение: {slow_time/fast_time:.1f} раз")

def test_edge_cases():
    print("\n" + "="*50)
    print("Тестирование крайних случаев")
    print("="*50)

    arr1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Тест 1: {arr1}, target={target1}")
    print(f"  Результат: {find_pair_fast(arr1, target1)} (ожидается (2, 7))")
    
    arr2 = [1, 2, 3, 4]
    target2 = 10
    print(f"\nТест 2: {arr2}, target={target2}")
    print(f"  Результат: {find_pair_fast(arr2, target2)} (ожидается None)")
    
    arr3 = [-1, 4, 7, -3, 9]
    target3 = 4
    print(f"\nТест 3: {arr3}, target={target3}")
    print(f"  Результат: {find_pair_fast(arr3, target3)} (ожидается (-3, 7))")
    
    arr4 = []
    target4 = 5
    print(f"\nТест 4: {arr4}, target={target4}")
    print(f"  Результат: {find_pair_fast(arr4, target4)} (ожидается None)")

if __name__ == "__main__":
    demonstrate_performance()
    demonstrate_intersection()
    test_edge_cases()



