class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = 0 
        self.salary = salary  
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            print(f"Ошибка: зарплата не может быть отрицательной ({value})!")
            return
        self._salary = value
        print(f"Зарплата {self.name} установлена: {value}")
    def __str__(self):
        return f"Сотрудник: {self.name}, зарплата: {self._salary}" 
    print()
print()
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"В отдел '{self.name}' добавлен: {employee.name}")
    def show_salaries(self):
        print(f"\nОтдел '{self.name}':")
        total = 0
        for emp in self.employees:
            print(f"  {emp.name}: {emp.salary}₽")
            total += emp.salary
        print(f"  Общий фонд зарплат: {total}₽")
        return total
    def increase_salaries(self, percent):
        print(f"\nПовышение зарплат на {percent}%:")
        for emp in self.employees:
            new_salary = emp.salary * (1 + percent / 100)
            emp.salary = new_salary
it_department = Department("IT")
employees_data = [
    ("Иван", 80000),
    ("Мария", 95000),
    ("Петр", 70000),
    ("Анна", 85000),
]
for name, salary in employees_data:
    emp = Employee(name, salary)
    it_department.add_employee(emp)
it_department.show_salaries()
it_department.increase_salaries(10)
it_department.show_salaries()