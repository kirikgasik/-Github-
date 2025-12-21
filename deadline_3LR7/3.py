from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
    def __str__(self):
        return f"Платежная система: {self.__class__.__name__}"
class CreditCardPayment(PaymentSystem):
    def __init__(self, card_number, card_holder):
        self.card_number = self._mask_card_number(card_number)
        self.card_holder = card_holder
    def _mask_card_number(self, card_number):
        return f"**** **** **** {card_number[-4:]}" if len(card_number) >= 4 else "****"
    def pay(self, amount):
        print(f" Оплата картой {self.card_number}")
        print(f"   Владелец: {self.card_holder}")
        print(f"   Сумма: {amount:.2f}₽")
        print(f"    Платеж проведен успешно!")
        return True
    def refund(self, amount):
        print(f" Возврат на карту {self.card_number}")
        print(f"   Владелец: {self.card_holder}")
        print(f"   Сумма: {amount:.2f}₽")
        print(f"    Возврат проведен успешно!")
        return True
    def __str__(self):
        return f"Кредитная карта ({self.card_number}, {self.card_holder})"
class PayPalPayment(PaymentSystem):
    def __init__(self, email):
        self.email = email
    def pay(self, amount):
        print(f" Оплата через PayPal")
        print(f"   Аккаунт: {self.email}")
        print(f"   Сумма: {amount:.2f}₽")
        print(f"    Перевод выполнен успешно!")
        return True
    def refund(self, amount):
        print(f" Возврат через PayPal")
        print(f"   Аккаунт: {self.email}")
        print(f"   Сумма: {amount:.2f}₽")
        print(f"    Возврат выполнен успешно!")
        return True
    def __str__(self):
        return f"PayPal ({self.email})"
    print()
print("Попытка создать экземпляр абстрактного класса PaymentSystem:")
try:
    ps = PaymentSystem()
    print("Успешно создан экземпляр PaymentSystem")
except TypeError as e:
    print(f" Ошибка: {e}")
    print("Это доказывает, что нельзя создать экземпляр абстрактного класса!")