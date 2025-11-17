def spiral_matrix(n):
    matrix = [[0]* n for _ in range(n)]
    x, y = n // 2, n // 2
    dx, dy = 0, 1
    length = 1
    num = 1

    matrix[x] [y] = num
    num += 1

    while num <= n * n:
        for _ in range(2):
                for _ in range(length):
                    if num > n * n:
                       break
                    x += dx
                    y += dy
                    matrix[x] [y] = num
                    num += 1
                dx, dy = -dy, dx
        if num > n * n:
            break
        length += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(''.join(f'{num:3}' for num in row))

print("Ввод: 5")
matrix_5 = spiral_matrix(5)
print("Вывод:")
print_matrix(matrix_5)

print("\nВвод: 3")
matrix_3 = spiral_matrix(3)
print("Вывод:") 
print_matrix(matrix_3)   
      