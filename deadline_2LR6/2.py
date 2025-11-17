def power(number, exponent=2):
    """
    Возводит число в указанную степень.
    Если степень не указана, возводит число в квадрат (степень2).
    """
    result = number ** exponent
    return result
result1 = power (5, 5)
print(f"5 в степени 5: {result1}")
result2 = power (10)
print(f"5 в квадрате: {result2}")
result3 = power(5,10)
print(f"5 в степени 10: {result3}")

