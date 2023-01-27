# Создать список с числами от 1 до 50 используя генератор списков
import random
a = [random.randint(1, 51) for i in range(10)]
print(a)