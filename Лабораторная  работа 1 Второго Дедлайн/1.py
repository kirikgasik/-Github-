count = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    count += 1
print("Количество введенных чисел до нуля", count)