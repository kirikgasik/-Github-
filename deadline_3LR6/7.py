from dataclasses import dataclass, field
from typing import ClassVar
@dataclass(frozen=True)
class Product:
    name: str
    price: float
    weight: float
    is_available: bool = True  
    currency_symbol: ClassVar[str] = "₽"  
    def order_cost(self, quantity: int) -> float:
        return self.price * quantity
    def __str__(self) -> str:
        status = "в наличии" if self.is_available else "нет в наличии"
        return f"{self.name}: {self.price:.2f}{self.currency_symbol}, {self.weight}кг ({status})"
    print()
products = [
    Product("Молоко", 85.50, 1.0, True),
    Product("Хлеб", 45.00, 0.5, True),
    Product("Шоколад", 120.00, 0.1, False),
    Product("Сыр", 350.00, 0.3, True),
    Product("Вода", 50.00, 1.5, True),
]
print("Список товаров:")
for product in products:
    print(f"  {product}")