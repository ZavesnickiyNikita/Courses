from random import *

a = [randint(1, 101) for i in range(10)]
b = tuple(a)
print(b)
print('min' , min(b), 'max', max(b))