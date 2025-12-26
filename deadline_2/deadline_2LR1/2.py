# Запрашиваем строку у пользователы
input_string = input("Введите строку: ")

#Подготавливаем строку: приводим к нижнему регистру и удаляем пробелы
cleaned_string = ""
index = 0
while index < len(input_string):
    char = input_string[index]
    if char.isalpha():
        cleaned_string += char.lower()
    index += 1
#Проверяем, является ли строка палиндромом 
is_palindrome = True 
start_index = 0
end_index = len(cleaned_string) - 1

while start_index < end_index:
    if cleaned_string[start_index] != cleaned_string[end_index]:
        is_palindrome = False
    start_index += 1
    end_index -= 1

#Выводим результат
if is_palindrome:
   print("Да, это палиндром")
else:
    print("Нет, это не палиндром")