def my_range(start, end, step=1):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
print()
for i in my_range(5, 2, -0.8):
    print(i)
        