a,b, c = map(int,input("Введите три целых числа через пробел: "). split())
res1 = a * b
res2 = b * c
res3 = c * a
res4 = a ** 4
res5 = b % c
res6 = c // a
sum_res = res4 + res5 + res6
print (f"Результаты умножения: {res1}, {res2} {res3} ")
print(f"Результаты дополнительных операций: {res4}, {res5}, {res6}")
print(f"Сумма результатов дополнительных операций: {sum_res}")
