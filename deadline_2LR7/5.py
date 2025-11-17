from typing import List, Any, Union
def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Находит общие элементы между двумя списками и возвращает их без дубликатов.
    Args:
        list1: Первый исходный список.
        list2: Второй исходный список.
    Returns:
        Новый список, содержащий только уникальные общие элементы.
    """
    # Преобразуем списки во множества для автоматического удаления дубликатов
    # и быстрого выполнения операции пересечения.
    set1 = set(list1)
    set2 = set(list2)
    # Используем операцию пересечения множеств (&)
    common_elements_set = set1 & set2
    # Преобразуем результирующее множество обратно в список для вывода
    return list(common_elements_set)
# --- Примеры вызова функции ---
list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]
common = find_common_elements(list1, list2)
print(f"Список 1: {list1}")
print(f"Список 2: {list2}")
print(f"Общие элементы: {common}") # Ожидаемый вывод: [4, 5] (порядок может отличаться)
print("-" * 20)
list_a = ["apple", "banana", "cherry", "apple"]
list_b = ["banana", "date", "cherry"]
common_strings = find_common_elements(list_a, list_b)
print(f"Общие фрукты: {common_strings}") # Ожидаемый вывод: ['banana', 'cherry'] (порядок может отличаться)

