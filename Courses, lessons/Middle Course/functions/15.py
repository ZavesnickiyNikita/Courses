import math


def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def root(num):
    return num ** 0.5

def absolute(num):
    return abs(num)

def sinus(num):
    return math.sin(num)


number = int(input())
dct = {'квадрат': square, 'куб': cube, 'корень': root, 'модуль': absolute, 'синус': sinus}
print(dct[input()](number))


