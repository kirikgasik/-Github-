class StringUtils:
    @staticmethod
    def invert(string):
        return string[::-1]
    @staticmethod
    def normalize(string):
        return string.strip().lower()
    @staticmethod
    def count_vowels(string):
        vowels = 'aeiouаеёиоуыэюя'
        return sum(1 for char in string.lower() if char in vowels)
    @staticmethod
    def is_palindrome(string):
        normalized = StringUtils.normalize(string).replace(" ", "")
        return normalized == normalized[::-1]
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    @classmethod
    def from_string(cls, data_string):
        if ";" not in data_string:
            raise ValueError("Строка должна содержать символ ';' для разделения")
        name, role = data_string.split(";", 1)  
        return cls(name.strip(), role.strip())
    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict.get('name', ''), data_dict.get('role', ''))
    def __str__(self):
        return f"User(name='{self.name}', role='{self.role}')"
    def __repr__(self):
        return f"User('{self.name}', '{self.role}')"
    print()
test_strings = ["Hello World", "А роза упала на лапу Азора", "Python", "Test123"]
print("Тестирование дополнительных методов StringUtils:")
for s in test_strings:
    print(f"\nСтрока: '{s}'")
    print(f"  Перевернутая: '{StringUtils.invert(s)}'")
    print(f"  Нормализованная: '{StringUtils.normalize(s)}'")
    print(f"  Гласных букв: {StringUtils.count_vowels(s)}")
    print(f"  Палиндром: {StringUtils.is_palindrome(s)}")