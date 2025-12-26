class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Животное издает звук")  
    def __str__(self):
        return self.name
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name}: Гав!")
    def wag_tail(self):
        print(f"{self.name} виляет хвостом!")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name}: Мяу!")
    def purr(self):
        print(f"{self.name} мурлычет...")
def animal_chorus(animals):
    for animal in animals:
        animal.make_sound()
class Farm:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.imals.append(animal)
        print(f"На ферму добавлено: {animal.name}")
    def morning_chorus(self):
        print("Утренний хор на ферме:")
        print("-" * 30)
        animal_chorus(self.animals)
        print("-" * 30)
    def feed_all(self):
        print(f"\nКормление {len(self.animals)} животных...")
        for animal in self.animals:
            print(f"{animal.name} кушает")
farm = Farm()
farm.animals = [
    Dog("Шарик"),
    Cat("Мурзик"),
    Dog("Тузик"),
    Cat("Рыжик"),
]
farm.morning_chorus()
farm.feed_all()