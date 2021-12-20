# программа,заполняющая матрицу змейкой
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        matrix[i][j] = 1 + count
        count += 1
count1 = 0
for i in range(n):
    count1 += 1
    if count1 % 2 == 0:
        matrix[i].reverse()
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
