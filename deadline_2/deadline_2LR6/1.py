def simple_calculator(num1, num2, operator):
    """
    Выполняет базовые математические операции (+, -, *, /) над двумя числами.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: Деление на ноль!"
    else:
        return "Ошибка: Неизвестный оператор. Используйте '+', '-', '*', или '/'."
result1 = simple_calculator(10, 5, '*')
print(f"10 * 5 = {result1}")
result2 = simple_calculator(20, 4, '/')
print(f"20 / 4 = {result2}")
result3 = simple_calculator(7, 3, '+')
print(f"7 + 3 = {result3}")
result4 = simple_calculator(10, 0, '/')
print(f"10 / 0 = {result4}")
result5 = simple_calculator(5, 5, '^')
print(f"5 ^ 5 = {result5}")

    

