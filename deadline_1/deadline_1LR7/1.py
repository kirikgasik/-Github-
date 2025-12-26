password = input("Введите пароль:")
confirm_pasword = input("Подтвердите пароль: ")

if password == confirm_pasword:
    saved_password = password 
    print("Пароль успешно установлен.")
    login_password = input("Введите  пароль для авторизации: ")
    if login_password == saved_password:
        print("Access")
    else:
        print("Denied")
else:
    print("Пароли не совпадают. Пожалуйста, попробуйте снова.")
    