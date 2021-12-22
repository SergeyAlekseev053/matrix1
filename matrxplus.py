# сложение матриц
import numpy as np

n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for j in range(n)]
input()
matrix2 = [[int(i) for i in input().split()] for j in range(n)]
a = np.array(matrix1)
b = np.array(matrix2)
temp = a + b
for i in temp:
    print(*i)
