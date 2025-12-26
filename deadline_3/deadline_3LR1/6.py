def squares_gen(n):
    for i in range(1, n + 1):
        yield i ** 5
gen = squares_gen(4)
for val in gen:
    print(val)