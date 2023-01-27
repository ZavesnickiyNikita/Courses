# Дана строка, в новый список добавить элементы, которые содержат пробел.
b = []
arr = ['hello my friend', 'my friend is', 'house', 'cat', 'dog']
for i in arr:
    if ' ' in i:
        b.append(i)
        print(b)