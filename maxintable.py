# Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы
n, m = int(input()), int(input())
matrix = [input().split() for i in range(n)]
max = -10000
stroka = 0
stolbets = 0
for i in range(n):
    for j in range(m):
        if int(matrix[i][j]) > max:
            stroka = i
            stolbets = j
            max = int(matrix[i][j])
print(stroka, stolbets)
