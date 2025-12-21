class SnakeCaseMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:
            if not attr_name.startswith("__") and any(c.isupper() for c in attr_name):
                raise TypeError(f"Метод {attr_name} должен быть написан в snake_case!")
        return super().__new__(cls, name, bases, dct)
class GoodCode(metaclass=SnakeCaseMeta):
    def get_data(self): pass  
try:
    class BadCode(metaclass=SnakeCaseMeta):
        def GetData(self): pass  
except TypeError as e:
    print(e)
class LimitMethodsMeta(type):
    def __new__(cls, name, bases, dct):
        methods = [k for k, v in dct.items() if callable(v) and not k.startswith("__")]
        if len(methods) > 3:
            raise TypeError(f"Класс {name} слишком сложный! Максимум 3 метода.")
        return super().__new__(cls, name, bases, dct)
try:
    class MyService(metaclass=LimitMethodsMeta):
        def one(self): pass
        def two(self): pass
        def three(self): pass
        def four(self): pass 
except TypeError as e:
    print(e)

