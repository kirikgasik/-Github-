import re
def analyze_text_with_sets():
    """
    Программа для анализа текста с использованием множеств.
    """
    user_input = input("Введите текст: ")
    words_list = re.findall(r'\b\w+\b', user_input.lower())
    if not words_list:
        print("Введенный текст не содержит слов для анализа.")
        return
    unique_words = set(words_list)
    print(f"\nУникальные слова: {len(unique_words)}")
    long_words = {word for word in unique_words if len(word) > 5}
    print(f"Длинные слова: {long_words}")
    keywords_to_check = {"python", "programming"}
    found_keywords = keywords_to_check.intersection(unique_words)
    is_keyword_present = bool(found_keywords)
    print(f"Найдены ключевые слова: {is_keyword_present}")
    if is_keyword_present:
        print(f"Найденные слова: {found_keywords}")
if __name__ == "__main__":
    analyze_text_with_sets()
