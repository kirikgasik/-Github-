from typing import Union
def sum_numbers(*args: Union[int, float]) -> Union[int, float]:
    """
    Вычисляет сумму произвольного количества числовых аргументов.
    Args:
        *args: Произвольное количество чисел (целых или с плавающей точкой).
    Returns:
        Сумма всех переданных чисел.
    """
    return sum(args)
result1 = sum_numbers(10,20,5)
print(f"Сумма чисел (10,20,5): {result1}")
result2 = sum_numbers(1.5, 2.5, 3)
print(f"Сумма чисел (1.5, 2.5, 3): {result2}")
