# заполнить диагонали и центральный столбец единицами
n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1
    for j in range(n):
        if i < j and i < n - 1 - j or i > j and i > n - 1 - j:
            matrix[i][j] = 1
for i in matrix:
    print(*i)
