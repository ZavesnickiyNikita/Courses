from random import *

a = [randint(0, 6) for i in range(20)]
b = [randint(0, 6) for i in range(20)]
a1 = tuple(a)
b2 = tuple(b)
c = a1 + b2
print(a1)
print(b2)
print(c)
print(c.count(0))  # Количество нулей
