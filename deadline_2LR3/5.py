from random import randint, random

class FruitStandCRM:
    def __init__(self, stand_name):
        self.stand_name = stand_name
        self.counter = {}  # На прилавке
        self.store = {}    # За прилавком
        self.prices = {}   # Цены
        self.money = 1000  # Стартовый капитал
        self.day = 1
        self.game_over = False
        
    def add_fruit(self, fruit_name, counter_max, store_max, sale_price, purchase_price):
        """Добавить новый фрукт в систему"""
        self.counter[fruit_name] = {'max': counter_max, 'current': 0}
        self.store[fruit_name] = {'max': store_max, 'current': 0}
        self.prices[fruit_name] = {'sale_price': sale_price, 'purchase_price': purchase_price}
    
    def restock_counter(self, fruit_name, amount):
        """Пополнить прилавок из запасов"""
        if fruit_name not in self.store:
            print(f"❌ Фрукт '{fruit_name}' не найден!")
            return False
        
        if self.store[fruit_name]['current'] < amount:
            print(f"❌ Недостаточно {fruit_name} за прилавком!")
            return False
        
        available_space = self.counter[fruit_name]['max'] - self.counter[fruit_name]['current']
        if available_space < amount:
            amount = available_space
        
        self.store[fruit_name]['current'] -= amount
        self.counter[fruit_name]['current'] += amount
        print(f"✅ Перемещено {amount} {fruit_name} на прилавок")
        return True
    
    def sell_fruit(self):
        """Попытка продажи фруктов за день"""
        sold_today = 0
        total_income = 0
        
        for fruit_name in list(self.counter.keys()):
            if self.counter[fruit_name]['current'] > 0:
                # Шанс продажи 60%
                if randint(1, 100) <= 60:
                    sell_amount = randint(1, min(3, self.counter[fruit_name]['current']))
                    self.counter[fruit_name]['current'] -= sell_amount
                    income = sell_amount * self.prices[fruit_name]['sale_price']
                    total_income += income
                    sold_today += sell_amount
                    print(f"💰 Продано {sell_amount} {fruit_name} за {income}₽")
        
        self.money += total_income
        return sold_today, total_income
    
    def ashot_theft(self):
        """Проверка на кражу Ашотом"""
        if randint(1, 100) <= 20:  # 20% шанс кражи
            stolen_fruits = {}
            total_loss = 0
            
            for fruit_name in list(self.counter.keys()):
                if self.counter[fruit_name]['current'] > 0:
                    steal_percent = randint(50, 100) / 100  # От 50% до 100%
                    stolen_amount = int(self.counter[fruit_name]['current'] * steal_percent)
                    if stolen_amount > 0:
                        self.counter[fruit_name]['current'] -= stolen_amount
                        loss = stolen_amount * self.prices[fruit_name]['sale_price']
                        total_loss += loss
                        stolen_fruits[fruit_name] = stolen_amount
            
            if stolen_fruits:
                print(f"\n🚨 АШОТ СТРАШНЫЙ УКРАЛ:")
                for fruit, amount in stolen_fruits.items():
                    print(f"   - {amount} {fruit}")
                print(f"💔 Общий ущерб: {total_loss}₽")
    
    def update_prices(self):
        """Изменение цен на фрукты"""
        print("\n📈 Изменение цен:")
        for fruit_name in self.prices:
            change_percent = randint(-15, 15) / 100  # -15% до +15%
            old_price = self.prices[fruit_name]['sale_price']
            new_price = max(1, int(old_price * (1 + change_percent)))
            self.prices[fruit_name]['sale_price'] = new_price
            change = "↑" if new_price > old_price else "↓" if new_price < old_price else "="
            print(f"   {fruit_name}: {old_price}₽ {change} {new_price}₽")
    
    def order_fruits(self, fruit_name, amount):
        """Заказ новых фруктов"""
        if fruit_name not in self.prices:
            print(f"❌ Фрукт '{fruit_name}' не найден!")
            return False
        
        cost = amount * self.prices[fruit_name]['purchase_price']
        if cost > self.money:
            print(f"❌ Недостаточно денег! Нужно {cost}₽, есть {self.money}₽")
            return False
        
        available_space = self.store[fruit_name]['max'] - self.store[fruit_name]['current']
        if available_space < amount:
            print(f"❌ Недостаточно места! Можно заказать только {available_space}")
            return False
        
        self.money -= cost
        self.store[fruit_name]['current'] += amount
        print(f"✅ Заказано {amount} {fruit_name} за {cost}₽")
        return True
    
    def display_status(self):
        """Показать текущее состояние"""
        print(f"\n{'='*50}")
        print(f"🏪 CRM система Ларька '{self.stand_name}' - День {self.day}")
        print(f"💰 Капитал: {self.money}₽")
        
        print(f"\n📊 НА ПРИЛАВКЕ:")
        for fruit, data in self.counter.items():
            print(f"   {fruit}: {data['current']}/{data['max']}")
        
        print(f"\n📦 ЗА ПРИЛАВКОМ:")
        for fruit, data in self.store.items():
            print(f"   {fruit}: {data['current']}/{data['max']}")
        
        print(f"\n🏷️ ЦЕНЫ (продажа/закупка):")
        for fruit, data in self.prices.items():
            print(f"   {fruit}: {data['sale_price']}₽/{data['purchase_price']}₽")
    
    def next_day(self):
        """Переход на следующий день"""
        self.day += 1
        
        # Продажи
        sold, income = self.sell_fruit()
        
        # Кража Ашотом
        self.ashot_theft()
        
        # Изменение цен
        self.update_prices()
        
        print(f"\n📊 Итоги дня {self.day-1}:")
        print(f"   Продано фруктов: {sold}")
        print(f"   Заработано: {income}₽")
        print(f"   Текущий капитал: {self.money}₽")
        
        # Проверка на банкротство
        if self.money <= 0:
            print(f"\n💀 БАНКРОТСТВО! Вы остались без денег!")
            self.game_over = True
            return False
        
        # Проверка на победу
        if self.day > 10:
            print(f"\n🎉 ПОБЕДА! Ашота поймали! Вы выжили 10 дней!")
            print(f"   Ваш финальный капитал: {self.money}₽")
            self.game_over = True
            return False
        
        return True

def main():
    print("🏪 Добро пожаловать в CRM систему Ларька!")
    stand_name = input("Введите название вашего ларька: ")
    
    crm = FruitStandCRM(stand_name)
    
    # Инициализация начальных фруктов
    crm.add_fruit("Яблоки", 20, 50, 15, 8)
    crm.add_fruit("Бананы", 15, 40, 25, 12)
    crm.add_fruit("Апельсины", 10, 30, 30, 15)
    crm.add_fruit("Арбузы", 5, 10, 100, 50)
    
    # Начальное заполнение запасов
    for fruit in crm.store:
        crm.store[fruit]['current'] = crm.store[fruit]['max'] // 2
    
    while not crm.game_over:
        crm.display_status()
        
        print(f"\n🎮 ДОСТУПНЫЕ ДЕЙСТВИЯ:")
        print("1. Пополнить прилавок")
        print("2. Заказать фрукты")
        print("3. Завершить день")
        print("4. Выйти из игры")
        
        choice = input("\nВыберите действие (1-4): ").strip()
        
        if choice == "1":
            fruit_name = input("Введите название фрукта: ").strip()
            if fruit_name in crm.counter:
                amount = int(input("Введите количество: "))
                crm.restock_counter(fruit_name, amount)
            else:
                print("❌ Фрукт не найден!")
        
        elif choice == "2":
            fruit_name = input("Введите название фрукта: ").strip()
            if fruit_name in crm.prices:
                amount = int(input("Введите количество: "))
                crm.order_fruits(fruit_name, amount)
            else:
                print("❌ Фрукт не найден!")
        
        elif choice == "3":
            if not crm.next_day():
                break
        
        elif choice == "4":
            print("👋 До свидания!")
            break
        
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()