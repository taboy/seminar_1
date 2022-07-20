#4Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
x1 = int(input("x1 - "))
y1 = int(input("y1 - "))
x2 = int(input("x2 - "))
y2 = int(input("y2 - "))
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('{:.3f}'.format(a), sep='')