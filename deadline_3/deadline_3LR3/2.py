def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) -1
    if low > high:
       return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid -1)
    else:
        return binary_search(arr, target, mid + 1, high) 
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(binary_search(names, "Charlie")) 
