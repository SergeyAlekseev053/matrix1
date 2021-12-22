# умножение матриц
import numpy as np

n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for j in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for j in range(m)]
a = np.array(matrix1)
b = np.array(matrix2)
temp = a.dot(b)
for i in temp:
    print(*i)
