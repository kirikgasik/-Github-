def task_1_short(arr):
    return 100 in arr
def task_2_short(arr):
    return arr[0] + arr[-1]
from collections import Counter
def task_3_fast(arr):
    return sum(v**2 for v in Counter(arr).values())