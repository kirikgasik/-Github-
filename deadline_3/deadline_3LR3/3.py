def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[:mid])
    return left_max if left_max > right_max else right_max
numbers = [6, 4, 2, 5, 9, 12]
print(find_max(numbers))
