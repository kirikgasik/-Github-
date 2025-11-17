def count_characters(text):
    """Подсчитывает количество каждого символа в строке без учета регистра."""
    char_count = {}
    
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count
text = input("Введите произвольный текст: ")
result = count_characters(text)
print(result)
