import string
from collections import Counter

def count_words():
    print("Введите текст (пустая строка для завершения):")
    
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    # Объединяем все строки и приводим к нижнему регистру
    text = ' '.join(lines).lower()
    
    # Удаляем пунктуацию
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    # Разбиваем на слова и подсчитываем
    words = text.split()
    word_counts = Counter(words)
    
    print(f"\nСтатистика слов:")
    for word, count in word_counts.most_common():
        print(f"'{word}': {count}")
    
    return dict(word_counts)

# Запуск программы
if __name__ == "__main__":
    result = count_words()