# программa, которая меняет местами элементы, стоящие на главной и побочной диагонали
n = int(input())
matrix = [input().split() for i in range(n)]
for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]
for i in matrix:
    print(*i)
