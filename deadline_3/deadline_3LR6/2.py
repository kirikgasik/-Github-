class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier
    def __call__(self, number):
        return self.multiplier * number
print()
multipliers = {
    "double": Multiplier(2),
    "triple": Multiplier(3),
    "quadruple": Multiplier(4),
    "half": Multiplier(0.5),
    "square": Multiplier(lambda x: x ** 2) 
}
test_numbers = [1, 2, 5, 10, 100]
for name, multiplier in multipliers.items():
    if name == "square":
        continue  
    print(f"\n{name.capitalize()}:")
    for num in test_numbers:
        result = multiplier(num)
        print(f"  {num} → {result}")    