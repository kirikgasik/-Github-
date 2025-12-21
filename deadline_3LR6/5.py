class Frange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0.0
            self.stop = float(start)
        else:
            self.start = float(start)
            self.stop = float(stop)
        self.step = float(step)
        if self.step == 0:
            raise ValueError("Шаг не может быть равен 0")
        self.current = self.start  
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        result = self.current
        self.current += self.step
        return result
    def __str__(self):
        return f"Frange({self.start}, {self.stop}, {self.step})"
    print()
print("1. Положительный шаг:")
for x in Frange(0, 1, 0.2):
    print(f"  {x:.1f}")
print("\n2. Отрицательный шаг:")
for x in Frange(5, 0, -1.5):
    print(f"  {x:.1f}")
print("\n3. Один аргумент (от 0 до значения):")
for x in Frange(2.5):
    print(f"  {x:.1f}")