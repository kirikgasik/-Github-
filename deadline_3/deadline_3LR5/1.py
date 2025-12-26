class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
         if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount:.2f}₽. Новый баланс: {self.balance:.2f}₽")
         else:
            print("Ошибка: сумма пополнения должна быть положительной!") 
    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной!")
            return False
        if amount > self.balance:
            print("Недостаточно средств!")
            return False
        self.balance -= amount
        print(f"Снятие: -{amount:.2f}₽. Новый баланс: {self.balance:.2f}₽")
        return True
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Счет: {self.account_holder}, Баланс: {self.balance:.2f}₽"
print()
account = BankAccount("Ivanov", 100)
account.deposit(50)
account.withdraw(200)  
account.withdraw(30)
print(f"Текущий баланс: {account.get_balance()}")