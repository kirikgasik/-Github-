students = [
   ("Иван",   19, 4.1),
   ("Анна",   21, 4.5),
   ("Петр",   22, 4.2),
   ("Мария",  20, 4.8),
   ("Сергей", 23, 3.9),
]

print(f"Исходный список студентов: {students}\n")
print("Студенты старше 20 лет:")

for name, age, grabe in students:
    if age > 20:
        print(f"-{name} ({age}), срелний балл: {grabe}")
best_student = max(students, key=lambda student: student[2])
best_name, best_age, best_grade = best_student

print(f"\nЛучший студент: {best_name}, средний балл: {best_grade}")

sorted_students_by_name = sorted(students, key=lambda student: student[0])

print("\nОтсортированный список студентов по имени:")

for name, age, grabe in sorted_students_by_name:
    print(f"- {name} (Возраст: {age}, Балл: {grabe})")
