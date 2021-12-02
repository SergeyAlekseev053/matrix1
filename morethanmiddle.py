# программа вычисляющая количество элементов в строке больше среднего значения в квадратной матрице
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
for i in matrix:
    summ = sum(i)
    count = 0
    for j in i:
        arif = summ / n
        if j > arif:
            count += 1
    print(count)
