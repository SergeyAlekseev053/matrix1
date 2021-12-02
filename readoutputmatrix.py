# программа для считывания и вывода матрицы
rows, cols = int(input()), int(input())
matrix = [[0] * cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = input()
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
