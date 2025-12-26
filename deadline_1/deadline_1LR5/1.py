text = input ("Введите произвольный текст: ")
s1, s2, = input("Введите две строки через  пробел: ").split()
formatted_text = text.replace(s1, s2)
print(formatted_text)