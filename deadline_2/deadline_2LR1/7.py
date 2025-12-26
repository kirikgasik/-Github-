def draw_filled_rectangle():
    """
    Задача 6: Рисует заполненный прямоугольный узор из заданного символа.
    Использует вложенные циклы while.
    """
    print("\n--- Задача 6: Заполненный прямоугольник ---")
    char_to_draw = input("Введите символ для рисования: ")
    try:
        height = int(input("Введите высоту прямоугольника: "))
        width = int(input("Введите ширину прямоугольника: "))
    except ValueError:
        print("Ошибка: Высота и ширина должны быть целыми числами.")
        return
    if height <= 0 or width <= 0:
        print("Ошибка: Высота и ширина должны быть больше нуля.")
        return
    print("\nВывод:")
    row_counter = 0
    while row_counter < height:
        col_counter = 0
        row_str = ""
        while col_counter < width:
            row_str += char_to_draw
            col_counter += 1
        print(row_str)
        row_counter += 1
def draw_hollow_rectangle():
    """
    Задача 7: Рисует полый (пустой внутри) прямоугольный узор.
    Использует вложенные циклы while и условную логику.
    """
    print("\n--- Задача 7: Полый прямоугольник ---")
    char_to_draw = input("Введите символ для рисования: ")
    try:
        height = int(input("Введите высоту прямоугольника: "))
        width = int(input("Введите ширину прямоугольника: "))
    except ValueError:
        print("Ошибка: Высота и ширина должны быть целыми числами.")
        return
    if height <= 0 or width <= 0:
        print("Ошибка: Высота и ширина должны быть больше нуля.")
        return
    print("\nВывод:")
    row = 0
    while row < height:
        col = 0
        row_str = ""
        while col < width:
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                row_str += char_to_draw
            else:
                row_str += " "
            col += 1
        print(row_str)
        row += 1
if __name__ == "__main__":
    draw_filled_rectangle()
    draw_hollow_rectangle()
