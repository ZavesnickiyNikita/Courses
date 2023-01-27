# 9.	Создать список. Проверить, есть ли в последовательности дубликаты
import random

a = [random.randint(1, 51) for i in range(20)]
print(a)
b = set(a)

if len(b) == len(a):
    print('Дубликатов нет')
else:
    print('Дубликаты есть')
