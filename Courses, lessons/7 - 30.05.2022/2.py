# Написать программу для вычисления значения выражений.
# a)
from math import *
# a = int(input())
#
# y = ((((1 + a + a ** 2) / (2 * a + a ** 2)) + 2 - ((1 - a + a ** 2) / (2 * a - a ** 2))) ** -1) * (5 - 2 * (a ** 2))
# print(y)

# b)
a = int(input())
b = int(input())
Y = int(input())

y = (1 / 4) * (sin(a + b - Y) + sin(b + Y - a) + sin(Y + a - b) - sin(a + b + Y))
print(y)
