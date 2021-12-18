# Напишите программу, которая создает матрицу размером n×m и заполняет её числами от 1 до n*m
n, m = [int(i) for i in input().split()]
matrix = [[1] * m for i in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = 1 + count
        count += 1
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
