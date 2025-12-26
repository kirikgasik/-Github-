def find_max(num1, num2):
    """
    Принимает два числа и возвращает большее из них.
    """
    if num1 > num2:
        return num1
    else:
        return num2
max_num1 = find_max(225, 15)
print(f"Большее число между 101 и 25: {max_num1}")
max_num2 = find_max(50, 120)
print(f"Большее число между 50 и 120: {max_num2}")
max_num3 = find_max(7, 7)
print(f"Большее число между 7 и 7: {max_num3}")