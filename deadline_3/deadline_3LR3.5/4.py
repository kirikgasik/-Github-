import sys
def create_list(n):
    return [x**2 for x in range(n)]
def create_gen(n):
    return (x**2 for x in range(n))
n = 1_000_000
lst = create_list(n)
gen = create_gen(n)
print(f"Размер списка из {n} элементов: {sys.getsizeof(lst)} байт")
print(f"Размер генератора: {sys.getsizeof(gen)} байт")

