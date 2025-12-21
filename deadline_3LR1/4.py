def safe_exec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
            return 0
    return wrapper
@safe_exec
def divide(a,b):
    return a / b
print(f"Результат 1: {divide(15,2)}")
print(f"Результат 1: {divide(25,0)}")