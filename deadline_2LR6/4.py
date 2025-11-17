def display_user_profile(name, age, city):
    """
    Выводит информацию о пользователе в отформатированном виде.
    """
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")
display_user_profile(age=21, name="Риван", city="Стрежевой")
print("-" * 20) 
display_user_profile(city="Нижневартовск", name="Кирилл", age=18)
