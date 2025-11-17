from typing import Dict, Any
def build_user_profile(user_id: int, **kwargs: Any) -> Dict[str, Any]:
    """
    Создает словарь профиля пользователя, объединяя обязательный user_id 
    с произвольным количеством дополнительной информации.
    Args:
        user_id: Обязательный уникальный идентификатор пользователя.
        **kwargs: Произвольное количество именованных аргументов 
                  (например, name, city, status).
    Returns:
        Словарь, содержащий все данные профиля.
    """
    profile_data = {'user_id': user_id}
    profile_data.update(kwargs)
    return profile_data
profile1 = build_user_profile(101, name="Кирилл", status="online", email="gasilov0305@gmail.com")
print(f"Профиль 1: {profile1}")
