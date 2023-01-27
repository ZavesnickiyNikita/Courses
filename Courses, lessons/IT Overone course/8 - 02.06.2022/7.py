a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
c = a + b
print(c)
c.insert(3, 6)
print(c)
for i in c:
    if type (i) is str:
        c.remove(i)
print(c)
print(len(c), 'Количество элементов списка')
c.sort()
print(c,   'Отсортированный список')