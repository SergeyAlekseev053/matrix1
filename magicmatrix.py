# программa, которая проверяет, является ли заданная квадратная матрица магическим квадратом(сумма всех строк,столбцов и диагоналей равна)
n = int(input())
m = [[int(i) for i in input().split()] for j in range(n)]
Flag = 'YES'
lmagic = [i for i in range(1, n ** 2 + 1)]
lst = []
for i in m:
    for j in i:
        lst.append(j)
lst1 = list(set(lst))
if lst1 != lmagic:
    Flag = 'NO'
summag = 0
for i in m[0]:
    summag += int(i)
sumrow = 0
for i in range(n):
    sumrow = 0
    for j in m[i]:
        sumrow += j
    if summag != sumrow:
        Flag = 'NO'
        break
for i in range(n):
    sumcol = 0
    for j in range(n):
        sumcol += m[j][i]
    if summag != sumcol:
        Flag = 'NO'
        break
diag1 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            diag1 += m[i][j]
diag2 = 0
for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            diag2 += m[i][j]
if diag2 != summag or diag1 != summag:
    Flag = 'NO'
print(Flag)
