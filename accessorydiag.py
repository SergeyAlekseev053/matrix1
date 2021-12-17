# программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:числа на побочной диагонали равны 1;числа, стоящие выше этой диагонали, равны 0;числа, стоящие ниже этой диагонали, равны 22.
n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            matrix[i][j] = 1
        if i < j and i > n - 1 - j or i > j and i > n - 1 - j or i == j and i > n - 1 - j:
            matrix[i][j] = 2

for i in matrix:
    print(*i)
