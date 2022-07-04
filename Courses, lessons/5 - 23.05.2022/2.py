# elements = [1, 3, 'a', 6, 'b']
#
# print(elements)
#
# a = (1, 2, 3)
# elements = list(a)         # Чаще всего применяется для переводи из любого другого типа в список
# print(elements)

# Создать список с элементами рандома
# объявим список и заполним его 10 рандомными элементами от 0 до 100
import random

c = [random.randint(0, 100) for i in range(10)]
print(c)

print(c[0])
print(c[-1])
print(c[5])
print(c[-4])
