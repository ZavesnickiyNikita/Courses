
#  6.	Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом
#  списке, так и во втором.
import random
first = [random.randint(1, 21) for i in range(10)]
second = [random.randint(1, 21) for i in range(10)]
print('Первый список', first,'\n', 'Второй список', second )


a1 = set(first)
a2 = set(second)
print('Повторяющиеся числа двух списков', a1 & a2)