# заполнение матрицы диагоналями
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
c = 1
l = 0
for i in range(m + n - 1):
    for j in range(n):
        if ((i - j) > -1) and ((i - j) < m):
            matrix[j][i - j] += c
            l += 1
            c += 1
    l = 0
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
