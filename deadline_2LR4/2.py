from math import sqrt
point_a = (3,7)
point_b = (10,2)
x1, y1 = point_a
x2, y2 = point_b
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Точка А: {point_a}")
print(f"Точка B: {point_b}")
print(f"Расстояние между точками: {distance:.2f}")
