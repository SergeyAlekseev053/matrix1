# программа, которая проверяет симметричность квадратной матрицы относительно главной диагонали
n = int(input())
matrix = []
Flag = 'YES'
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            Flag = 'NO'
            break
print(Flag)
