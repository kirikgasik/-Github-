def draw_rectangle():
    """
    Рисует прямоугольный узор из заданного символа, используя вложенные циклы while.
    """
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
    print(f"\n--- Ваш прямоугольник {height}x{width} ---")
    row_counter = 0
    while row_counter < height:
        col_counter = 0
        row_str = "" 
        while col_counter < width:
            row_str += char_to_draw
            col_counter += 1
        print(row_str)
        row_counter += 1
if __name__ == "__main__":
    draw_rectangle()
