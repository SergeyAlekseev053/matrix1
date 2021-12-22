# возведение матрицы в степень
import numpy as np

n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
m = int(input())
a = np.array(matrix)
res = np.linalg.matrix_power(matrix, m)
for i in res:
    print(*i)
