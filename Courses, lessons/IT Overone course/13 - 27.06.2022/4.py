# 7.	Создать кортеж с числами от 1 до 50 используя генератор списков
import random

a = [random.randint(1, 51) for i in range(15)]
b = tuple(a)
print(b)
print(type(b))
