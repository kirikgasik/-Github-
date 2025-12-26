
math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}
print(f"Математика: {math_students}")
print(f"Физика:    {physics_students}")
print(f"CS:        {cs_students}\n")
all_three_courses = math_students & physics_students & cs_students
print(f"Все три курса: {all_three_courses}")
all_students = math_students | physics_students | cs_students 
two_courses_plus = (math_students & physics_students) | \
                   (math_students & cs_students) | \
                   (physics_students & cs_students)
only_one_course = all_students - two_courses_plus
only_math = math_students - physics_students - cs_students
only_physics = physics_students - math_students - cs_students
only_cs = cs_students - math_students - physics_students
only_one_course_exact = only_math | only_physics | only_cs
print(f"Только один курс: {only_one_course_exact}")
math_but_not_physics = math_students - physics_students
print(f"Математика, но не физика: {math_but_not_physics}")
total_unique_students = len(all_students)
print(f"Всего студентов: {total_unique_students}")
