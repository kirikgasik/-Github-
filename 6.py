def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
print(f"2 в степени 3: {power(2, 3)}") 
print(f"5 в степени 0: {power(5, 0)}") 
print(f"3 в степени 4: {power(3, 4)}")
