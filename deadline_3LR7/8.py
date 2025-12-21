from typing import Callable, Any
from functools import wraps
def audit_log(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(self, amount: float) -> Any:
        result = func(self, amount)
        print(f'Выполнена операция "{func.__name__}". Сумма: {amount}')
        return result
    return wrapper
class BankAccount:
    def __init__(self, initial_balance: float = 0.0) -> None:
        self._balance = initial_balance
        print(f"Создан счет с начальным балансом: {initial_balance}")
    @audit_log
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
    @audit_log
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= amount
    def balance(self) -> float:
        return self._balance
    def __str__(self) -> str:
        return f"BankAccount(баланс: {self._balance})"
def main() -> None:
    print("=== Демонстрация работы банковского счета ===\n")
    account = BankAccount(1000.0)
    print(f"Текущий баланс: {account.balance()}\n")
    try:
        account.deposit(500.0)
        print(f"Баланс после пополнения: {account.balance()}\n")
        account.withdraw(300.0)
        print(f"Баланс после снятия: {account.balance()}\n")
        print("Попытка снять 1500.0:")
        account.withdraw(1500.0)
    except ValueError as e:
        print(f"Ошибка: {e}\n")
    account.deposit(200.0)
    print(f"Итоговый баланс: {account.balance()}\n")
    try:
        print("Попытка пополнить на -100.0:")
        account.deposit(-100.0)
    except ValueError as e:
        print(f"Ошибка: {e}\n")
    try:
        print("Попытка снять -50.0:")
        account.withdraw(-50.0)
    except ValueError as e:
        print(f"Ошибка: {e}\n")
    print(f"Финальный баланс: {account.balance()}")
    print(account)
if __name__ == "__main__":
    main()
