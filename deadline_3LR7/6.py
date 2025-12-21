class Vector3D:
    __slots__ = ('x', 'y', 'z')  
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
v = Vector3D(1, 2, 3)
try:
    print(v.__dict__)
except AttributeError:
    print("У объекта нет атрибута __dict__ (память оптимизирована)")
try:
    v.color = "Red"
except AttributeError as e:
    print(f"Ошибка: {e} (нельзя добавить 'color')")
class User:
    __slots__ = ('user_id', 'username')
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
users = [User(i, f"user_{i}") for i in range(1000)]
print(f"Создано {len(users)} объектов с оптимизацией памяти.")

