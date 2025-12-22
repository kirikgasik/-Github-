import time
n = 100_000
iterations = 1000
test_list_start = list(range(n))
start_time = time.time()
for _ in range(iterations):
    test_list_start.pop(0)
end_time = time.time()
time_pop_0 = end_time - start_time
test_list_end = list(range(n))
start_time = time.time()
for _ in range(iterations):
    test_list_end.pop()
end_time = time.time()
time_pop_end = end_time - start_time
print(f"Удаление из начала (pop(0)) 1000 раз: {time_pop_0:.6f} сек.")
print(f"Удаление с конца (pop()) 1000 раз: {time_pop_end:.6f} сек.")