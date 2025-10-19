import random
import string

def generate_random_string(length: int) -> str:
    "Генерирует случайную строку из букв ASCII и цифр."
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = "".join(random.choice(characters) for i in range(length))
    return random_string
# Ввод данных от пользователя 
message = input ("Введите сообщение: ")
n = int(input("Введите число n (количество подстановочных символов): "))

#Кодирование сообщения
encoded_parts = []
for char in message:
    random_chars = generate_random_string(n)
    encoded_parts.append(char + random_chars)

#Объединение частей в одно сообщение
encoded_message = "".join(encoded_parts)

#Вывод результата
print("Полученное кодированное послание:")
print(encoded_message)

