# программa для создания матрицы размером n×m, заполняя её символами . и * в шахматном порядке
n, m = [int(i) for i in input().split()]
matrix = [['*'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = '.'
for i in matrix:
    print(*i)
