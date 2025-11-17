import re
from collections import Counter

def analyze_text():
    """
    Программа для статистического анализа введенного пользователем текста.
    """
    print("Пожалуйста, введите текст. Для завершения ввода нажмите Enter дважды.")
    
    # 1. Пользователь вводит произвольный текст (многострочный ввод)
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    raw_text = "\n".join(lines)
    
    # 2. Программа должна:
    
    # Разбить текст на слова (игнорируя знаки препинания)
    # Используем регулярное выражение для поиска всех последовательностей букв и цифр
    # re.findall находит все непересекающиеся совпадения с шаблоном.
    words = re.findall(r'\b\w+\b', raw_text.lower())
    
    if not words:
        print("\nТекст не содержит слов для анализа.")
        return

    # Создать список слов в нижнем регистре (сделано выше, при re.findall(..., raw_text.lower()))
    
    # Найти самое длинное и самое короткое слово
    # Используем функции min/max с ключом len для поиска по длине
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    
    # Посчитать среднюю длину слова
    average_length = sum(len(word) for word in words) / len(words)
    
    # Вывести 5 самых частых слов
    # Используем collections.Counter для подсчета частоты слов
    word_counts = Counter(words)
    top_5_frequent = word_counts.most_common(5)
    
    # --- Вывод результатов ---
    print("\n--- Результаты анализа текста ---")
    print(f"Общее количество слов: {len(words)}")
    print(f"Самое длинное слово:  '{longest_word}' (длина: {len(longest_word)})")
    print(f"Самое короткое слово: '{shortest_word}' (длина: {len(shortest_word)})")
    print(f"Средняя длина слова:  {average_length:.2f}")
    
    print("\n5 самых частых слов:")
    for word, count in top_5_frequent:
        print(f"- '{word}': {count} раз(а)")

# Запускаем программу
if __name__ == "__main__":
    analyze_text()
