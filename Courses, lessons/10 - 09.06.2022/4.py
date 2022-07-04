# создать множество

a = set([1, 2, 3, 4, 'one', 'two'])  # Изменяемое множество

b = frozenset([5, 6, 7, 8, 'three', 'two'])  # Неизменяемое множество

c = a.union(b)  # Объединение двух множеств
print(c)
print(a | b)

print(a & b)  # Пересечение множеств
