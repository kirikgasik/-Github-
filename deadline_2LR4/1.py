import random
original_list = [random.randint(1, 100) for _ in range(10)]
even_numbers = [num for num in original_list if num % 2 == 0]
numbers_greater_than_50 = [num for num in original_list if num > 50]
print(f"Исходный список случайных чисел: {original_list}")
print(f"Список четных числе: {even_numbers}")
print(f"Список чисел больше 50: {numbers_greater_than_50}")