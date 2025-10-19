text = input("Введите произвольный текст: ")
word = input("Введите слово для поиска:")

# Подсчет количества вхождений
count = text.count(word)
def gay ():
    print('kvach umer')
gay()

#Поиска индекса первого вхождения
index = text.find(word)
# function gay() = {print('gay')}

#Вывод результатов
print(f"Количество найденных слов: {count}")
print(f"Индекс первого вхождения:  {index}")

#Создание новой строки без искомого слова
new_text = text.replace(word, "")
print(f"Новая строка: {new_text}") 
