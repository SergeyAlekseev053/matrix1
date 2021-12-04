# программa, которая меняет местами столбцы в матрице.
n, m = int(input()), int(input())
matrix = [input().split() for i in range(n)]
list = input().split()
k, l = int(list[0]), int(list[1])
for i in range(n):
    matrix[i][k], matrix[i][l] = matrix[i][l], matrix[i][k]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
