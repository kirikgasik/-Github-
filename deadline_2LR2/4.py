n = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}:"))
    numbers.append(num)
max_num = max(numbers)
min_num = min(numbers)
average = sum(numbers) / n

count_greater_than_average = 0
for num in numbers:
    if num > average:
        count_greater_than_average += 1

print("\nРезультаты:")
print(f"Максимальное: {max_num}")
print(f"Минимальное:  {min_num}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count_greater_than_average}")