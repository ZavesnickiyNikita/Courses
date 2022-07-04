# d = {1: 2, 2: 4, 3: 9, 5:{1: 2, 2: 2, 3: 3, 4:4}}
# d[4] = 4 ** 2
# print(d)

# Копия словаря
# a = d.copy()
# print(a)
# Выводит и ключи и значения
# print(d.items())
# Выводит только ключи
# print(d.keys())

# Указываем ключ в (). Удаляет по ключу, а выводит удаленное значение.
# print(d.pop(1))
# print(d)

# Выводит только значения
# print(d.values())

# Выводит количество только ключей
# print(len(d))

# del d[1]
# print(d)

# Проверка наличия элементов в словаре

# c = 2 in d
# print(c)

# Создание словаря функцией ZIP из списка ключей и значений

# numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
# print(numbers)

# Цикл for по словарю

Months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr'}
for i in Months:
    print(i,': ', Months[i])