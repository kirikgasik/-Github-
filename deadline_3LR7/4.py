class LoggableMixin:
    def log(self, message):
        class_name = self.__class__.__name__
        print(f"[INFO] {class_name}: {message}")
    def log_warning(self, message):
        class_name = self.__class__.__name__
        print(f"[WARNING] {class_name}: {message}")
    def log_error(self, message):
        class_name = self.__class__.__name__
        print(f"[ERROR] {class_name}: {message}")
print()
class Employee(LoggableMixin):
    def __init__(self, name, salary):
        self.name = name
        self._salary = 0
        self.salary = salary
        self.log(f"Сотрудник {name} создан")
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            self.log_error(f"Попытка установить отрицательную зарплату: {value}")
            print("Ошибка: зарплата не может быть отрицательной!")
            return
        old_salary = self._salary
        self._salary = value
        if old_salary != 0:  
            self.log(f"Зарплата изменена: {old_salary} -> {value}")
        else:
            self.log(f"Зарплата установлена: {value}")
    def promote(self, new_salary):
        self.log(f"Повышение сотрудника {self.name}")
        self.salary = new_salary
    def __str__(self):
        return f"Сотрудник: {self.name}, зарплата: {self._salary}"
emp = Employee("Manager", 50000)
emp.log("Сотрудник успешно создан")
emp.salary = 55000
emp.salary = -1000  
emp.promote(60000)
