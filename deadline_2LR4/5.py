import random

def print_field(field):
    """Вывод игрового поля"""
    print("\n   0 1 2")
    for i, row in enumerate(field):
        print(f"{i}  {' '.join(row)}")

def check_win(field, player):
    """Проверка победы"""
    # Проверка строк
    for row in field:
        if all(cell == player for cell in row):
            return True
    
    # Проверка столбцов
    for col in range(3):
        if all(field[row][col] == player for row in range(3)):
            return True
    
    # Проверка диагоналей
    if all(field[i][i] == player for i in range(3)):
        return True
    if all(field[i][2-i] == player for i in range(3)):
        return True
    
    return False

def check_draw(field):
    """Проверка ничьей"""
    for row in field:
        if ' ' in row:
            return False
    return True

def computer_move(field):
    """Ход компьютера"""
    # Сначала проверяем выигрышные ходы
    for i in range(3):
        for j in range(3):
            if field[i][j] == ' ':
                field[i][j] = 'O'
                if check_win(field, 'O'):
                    return i, j
                field[i][j] = ' '
    
    # Затем блокируем выигрышные ходы противника
    for i in range(3):
        for j in range(3):
            if field[i][j] == ' ':
                field[i][j] = 'X'
                if check_win(field, 'X'):
                    field[i][j] = 'O'
                    return i, j
                field[i][j] = ' '
    
    # Случайный ход
    empty_cells = [(i, j) for i in range(3) for j in range(3) if field[i][j] == ' ']
    return random.choice(empty_cells)

def play_game():
    """Основная функция игры"""
    field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'
    
    print("Добро пожаловать в Крестики-нолики!")
    print("Выберите режим:")
    print("1 - Игра против человека")
    print("2 - Игра против компьютера")
    
    mode = input("Ваш выбор (1/2): ")
    vs_computer = (mode == "2")
    
    while True:
        print_field(field)
        
        if vs_computer and current_player == 'O':
            print("\nХод компьютера (O):")
            row, col = computer_move(field)
        else:
            print(f"\nХод игрока {current_player}:")
            try:
                coords = input("Введите координаты (строка,столбец): ").split(',')
                row, col = int(coords[0]), int(coords[1])
            except:
                print("Ошибка! Введите координаты в формате: 0,1")
                continue
        
        # Проверка корректности хода
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Координаты должны быть от 0 до 2!")
            continue
        
        if field[row][col] != ' ':
            print("Эта клетка уже занята!")
            continue
        
        # Выполнение хода
        field[row][col] = current_player
        
        # Проверка победы
        if check_win(field, current_player):
            print_field(field)
            if vs_computer and current_player == 'O':
                print("Компьютер победил!")
            else:
                print(f"Игрок {current_player} победил!")
            break
        
        # Проверка ничьей
        if check_draw(field):
            print_field(field)
            print("Ничья!")
            break
        
        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

# Запуск игры
if __name__ == "__main__":
    play_game()
