def calc_avg(numbers: list[int | float]) -> float:
    """
    Вычисляет среднее арифметическое значение списка чисел.
    Args:
        numbers: Список целых или вещественных чисел
    Returns:
        Среднее арифметическое значение. Возвращает 0.0 для пустого списка
    Examples:
        >>> calc_avg([10, 20, 30, 40])
        25.0
        >>> calc_avg([])
        0.0
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    """
    Форматирует ФИО из списка составляющих частей.
    Args:
        parts: Список строк, представляющих фамилию, имя и отчество
        capitalize: Флаг, указывающий нужно ли применять капитализацию 
                   (каждое слово с заглавной буквы). По умолчанию True
    Returns:
        Отформатированная строка с ФИО
    Examples:
        >>> fmt_fio(["петров", "иван", "сергеевич"])
        'Петров Иван Сергеевич'
        >>> fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False)
        'сидорова анна валерьевна'
    """
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio

def filter_scores(data_dict: dict[str, int | float], min_value: int | float) -> dict[str, int | float]:
    """
    Фильтрует словарь, оставляя только элементы со значениями не меньше заданного порога.
    Args:
        data_dict: Словарь, где ключи - строки, значения - числа
        min_value: Минимальное пороговое значение для фильтрации
    Returns:
        Новый словарь, содержащий только элементы с значениями >= min_value 
    Examples:
        >>> scores = {"math": 95, "history": 78, "english": 88, "art": 92}
        >>> filter_scores(scores, 90)
        {'math': 95, 'art': 92}
    """
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value    
    return result
if __name__ == "__main__":
    # Примеры использования функции 1
    print("=== Функция calc_avg ===")
    print(f"calc_avg([10, 20, 30, 40]) = {calc_avg([10, 20, 30, 40])}")
    print(f"calc_avg([1.5, 2.5, 3.5]) = {calc_avg([1.5, 2.5, 3.5])}")
    print(f"calc_avg([]) = {calc_avg([])}")
    print()
    # Примеры использования функции 2
    print("=== Функция fmt_fio ===")
    print(f"fmt_fio(['петров', 'иван', 'сергеевич']) = '{fmt_fio(['петров', 'иван', 'сергеевич'])}'")
    print(f"fmt_fio(['сидорова', 'анна', 'валерьевна'], capitalize=False) = '{fmt_fio(['сидорова', 'анна', 'валерьевна'], capitalize=False)}'")
    print(f"fmt_fio(['СМИТ', 'джон', 'майкл']) = '{fmt_fio(['СМИТ', 'джон', 'майкл'])}'")
    print()
    # Примеры использования функции 3
    print("=== Функция filter_scores ===")
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    print(f"Исходные данные: {scores}")
    print(f"filter_scores(scores, 90) = {filter_scores(scores, 90)}")
    print(f"filter_scores(scores, 80) = {filter_scores(scores, 80)}")
    # Дополнительный пример с вещественными числами
    temperatures = {"утро": 15.5, "день": 22.3, "вечер": 18.7, "ночь": 12.1}
    print(f"Температуры: {temperatures}")
    print(f"filter_scores(temperatures, 16.0) = {filter_scores(temperatures, 16.0)}")
