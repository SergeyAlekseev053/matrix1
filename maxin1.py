# программы вычисляющая максимальное значение в первой четверти квадратной матрицы
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
maximum = -1000
for i in range(n):
    for j in range(n):
        if i < j:
            continue
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
