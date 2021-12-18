# программу, которая создает матрицу размером n×m заполнив её в соответствии с образцом
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
count = 0
for i in range(n):
    count = 0
    for j in range(m):
        matrix[i][j] = 1 + count + i
        count += n
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
