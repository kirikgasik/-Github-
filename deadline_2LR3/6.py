grades = []
grades.append (4)
grades.append (5)
grades.append (3)
grades.append (4)
grades.append (5)
print(f"Текущий оценки: {grades}")

grades.pop(0)
grades.pop(-1)

average_grade = sum(grades) / len(grades)
print(f"Средний балл студентов: {average_grade:.2f}")
print(f"Итоговый список оценок: {grades}")