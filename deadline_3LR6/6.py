class Person:
    def __init__(self, name, age):
        super().__setattr__('name', name)
        super().__setattr__('age', age)
    def __setattr__(self, name, value):
        if name == 'age':
            if value < 0:
                print("Нельзя быть младше 0")
                value = 0
            elif value > 150:  
                print("Введен нереалистичный возраст")
                value = 150
        super().__setattr__(name, value)
    def __getattr__(self, name):
        return None
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    print()
person1 = Person("Анна", 25)
print(f"Создан: {person1}")
person1.age = -10
print(f"После установки -10: {person1}")
person1.age = 35
print(f"После установки 35: {person1}")
person1.age = 200
print(f"После установки 200: {person1}")
print(f"\nНесуществующие атрибуты:")
print(f"  person1.job = {person1.job}")
print(f"  person1.address = {person1.address}")
print(f"  person1.phone = {person1.phone}")
