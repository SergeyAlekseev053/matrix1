# разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for i in range(n):
        matrix[i][i] = 1
        matrix[i][n - i - 1] = 1
for i in matrix:
    print(*i)
