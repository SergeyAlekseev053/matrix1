# программa, которая зеркально отображает её элементы относительно горизонтальной оси симметрии
n = int(input())
matrix = [input().split() for i in range(n)]
m2 = matrix[::-1]
for i in m2:
    print(*i)


