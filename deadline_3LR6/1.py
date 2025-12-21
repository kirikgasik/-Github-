class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Можно складывать только векторы с векторами")
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Можно вычитать только векторы из векторов")
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Можно вычитать только векторы из векторов")
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other  
        raise TypeError("Можно умножать вектор только на число или другой вектор")
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def dot(self, other):
        if isinstance(other, Vector):
            return self * other
        raise TypeError("Аргумент должен быть вектором")
    def scale(self, factor):
        return Vector(self.x * factor, self.y * factor)
    print()
vectors = [
    Vector(1, 2),
    Vector(3, 4),
    Vector(-1, 5),
    Vector(0, 0),
    Vector(2.5, 3.7)
]
print("Список векторов:")
for v in vectors:
    print(f"  {v}")
print("\nОперации с векторами:")
v_a = Vector(3, 4)
v_b = Vector(1, -1)
v_c = Vector(2, 0)
print(f"v_a = {v_a}")
print(f"v_b = {v_b}")
print(f"v_c = {v_c}")
print(f"\nv_a + v_b + v_c = {v_a + v_b + v_c}")
print(f"v_a - v_b = {v_a - v_b}")
print(f"v_b * 2.5 = {v_b * 2.5}")
print(f"v_a * v_b = {v_a * v_b} (скалярное произведение)")
print(f"|v_a| = {abs(v_a):.2f}")
print(f"|v_b| = {abs(v_b):.2f}")