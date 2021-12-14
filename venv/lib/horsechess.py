# программa, которая отмечает положение коня на доске и все клетки, которые бьет конь
x, y = input()
m = [['.'] * 8 for i in range
(8)]
col = ('abcdefgh')
row = ('87654321')
m[row.find(y)][col.find(x)] = 'N'
for i in range(8):
    for j in range(8):
        INX = (col.find(x) - i) * (row.find(y) - j)
        if INX == 2 or INX == -2:
            m[j][i] = '*'
for i in m:
    print(*i)
