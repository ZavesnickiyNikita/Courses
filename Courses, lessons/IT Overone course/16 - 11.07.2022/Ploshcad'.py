import math
def circle(r):
    s = math.pi * (r ** 2)
    return s

def rectangle():
    s = a * b
    return s

def triangle():
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

answer = input('Площадь чего Вы хотите посчитать? (круг, Квадрат, прямоугольник)')
if answer == 'круг'.lower():
    r = int(input('Введите радиус (r)'))
    print(circle(r))
elif answer == 'треугольник'.lower():
    a, b, c = int(input('Сторона a')), int(input('Сторона b')), int(input('Сторона c'))
    print(triangle())
elif answer == 'прямоугольник'.lower():
    a, b = int(input('Сторона a')), int(input('Сторона b'))
    print(rectangle())
