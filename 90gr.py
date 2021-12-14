# программa, которая поворачивает квадратную матрицу чисел на по 90 градусов часовой стрелке.
n = int(input())
m = [input().split() for i in range(n)]
rotated = zip(*m[::-1])
rotated = tuple(zip(*m[::-1]))
for i in rotated:
    print(*i)
