# программa для создания матрицы размером n×m, заполняя её символами . и * в шахматном порядке
res = input().split()
n = int(res[0])
m = int(res[1])
matrix = [['*'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = '.'
for i in matrix:
    print(*i)
