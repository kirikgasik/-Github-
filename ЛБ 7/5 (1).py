import math
#Получение ввода от пользователя 
user_input = input("Введите число 1, знак и число 2 через пробел: ")
num1_str, operator, num2_str = user_input.split()

#Преобразование строк в числа
num1 = float(num1_str)
num2 = float(num2_str)

#Выполнение операции в зависимости от знака 
if operator == '*':
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '%':
    result = num1 % num2
elif operator == '//':
    result = num1 // num2
elif operator == '**':
    result = num1 ** num2
elif operator == '%%':
    result = (num2 / 100) * num1
elif operator == '/**':
    result = math.sqrt(num1)
else:
    result = "Неверный знак операции"

#Вывод результата
print("Результат:", result)