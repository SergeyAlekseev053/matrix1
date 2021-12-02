# программа вычисляющая максимальное значение из двух четвертей квадратной матрицы ><
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
maximum = -100
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j or i > j and i > n - 1 - j:
            continue
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
print(maximum)
