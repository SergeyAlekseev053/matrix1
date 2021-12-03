# программa, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
over = 0
lower = 0
left = 0
right = 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            over += matrix[i][j]
        if i < j and i > n - 1 - j:
            right += matrix[i][j]
        if i > j and i > n - 1 - j:
            lower += matrix[i][j]
        if i > j and i < n - 1 - j:
            left += matrix[i][j]
print('Верхняя четверть:', over)
print('Правая четверть:', right)
print('Нижняя четверть:', lower)
print('Левая четверть:', left)
