import functools
def logger(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args} {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"Результат: {result}")
            return result
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise 
    return wrapper
@logger
def greet(name="Мир", greeting="Привет"):
    return f"{greeting}, {name}!"
print("\n--- Тест greet ---")
greet("Алиса")
greet(greeting="Здравствуйте", name="Борис")