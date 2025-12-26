import sys
def phone_book_app():
    """
    Простая интерактивная телефонная книга с использованием словаря.
    """
    phone_book = {
        "Иван": "+79991234567",
        "Мария": "+79123456789",
        "Петр": "+79011112233"
    }
    print("Добро пожаловать в телефонную книгу!")
    while True:
        print("\n--- Меню ---")
        print("1 - Показать все контакты")
        print("2 - Добавить контакт")
        print("3 - Удалить контакт")
        print("4 - Выйти")
        print("------------")
        choice = input("Выберите действие (1-4): ")
        if choice == '1':
            # 1 - Показать все контакты
            print("\n*** Ваши контакты ***")
            if not phone_book:
                print("Телефонная книга пуста.")
            else:
                for name, phone in phone_book.items():
                    print(f"Имя: {name}, Телефон: {phone}")
        elif choice == '2':
            # 2 - Добавить контакт
            print("\n*** Добавление контакта ***")
            name = input("Введите имя нового контакта: ").strip()
            if not name:
                print("Имя не может быть пустым.")
                continue   
            if name in phone_book:
                print(f"Ошибка: Контакт с именем '{name}' уже существует.")
            else:
                phone = input(f"Введите номер телефона для {name}: ").strip()
                if not phone:
                     print("Номер телефона не может быть пустым.")
                     continue
                phone_book[name] = phone
                print(f"Контакт '{name}' успешно добавлен.")
        elif choice == '3':
            # 3 - Удалить контакт
            print("\n*** Удаление контакта ***")
            name = input("Введите имя контакта для удаления: ").strip()
            
            if name in phone_book:
                del phone_book[name]
                print(f"Контакт '{name}' успешно удален.")
            else:
                print(f"Ошибка: Контакт с именем '{name}' не найден в книге.")
        elif choice == '4':
            print("Выход из программы. До свидания!")
            sys.exit() # Завершает программу
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 4.")
if __name__ == "__main__":
    phone_book_app()

