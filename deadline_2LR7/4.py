from typing import Any, Dict, List
def format_report(report_title: str, *data: str, **properties: Any) -> None:
    """
    Форматирует и выводит отчет, включающий название, пункты данных и метаданные
    Args:
        report_title: Обязательное название отчета.
        *data: Произвольное количество позиционных аргументов (пункты данных).
        **properties: Произвольное количество именованных аргументов (метаданные).
    """
    print(f"\n--- Отчет: {report_title} ---")
    if data:
        print("Данные:")
        for item in data:
            print(f" - {item}")
    else:
        print("Данные отсутствуют.")
    if properties:
        print("\nСвойства:")
        for key, value in properties.items():
            print(f" - {key}: {value}")
    else:
        print("Свойства отсутствуют.")
    print("------------------------------")
format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Гасилов К.П.",
    date="2025-11-04"
)
format_report(
    "Ежемесячный бюджет",
    manager="Дамиров Р.Р.",
    status="Утвержден"
)
format_report(
    "Список задач на день",
    "Задача 1: Код",
    "Задача 2: Тесты",
    "Задача 3: Обед"
)
