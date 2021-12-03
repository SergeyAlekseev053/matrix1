# программа создает матрицу mult размером n*m и заполняет её таблицей умножения по формуле mult[i][j] = i * j
n, m = int(input()), int(input())
mult = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()
