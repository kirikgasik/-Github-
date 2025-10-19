text = input("Введите текст: ")
start, end = map(int, input("Введите диапазон (например, 3 7):").split())

start_index = start - 1
end_index = end

substring = text[start_index:end_index]
print(f"Результат: {substring}")