num_set = {1, 2, 3, 4, 5, 6}
print(num_set)

# Cпособы создания множества
num_set = set([1, 2, 3, 4, 5, 6])
print(num_set)

# Определить создан словарь или множество

x = {}
print(type(x))

# Создать пустое множество
x = set()
print(type(x))

# Циклы в множествах
monts = set(['Jan', 'Feb', 'Mar', 'Apr'])
for i in monts:
    print(i)

# Позволяет проверить наличие элементов в множестве
print('Jan' in monts)


# Добавление элементов во множество
monts.add('May')
print(monts)

# Удаление элементов discard или remove
# Когда используем discard, то если элемента нет, не будет ошибка, а если использовать
# remove, если элемента нет, то ошибка будет
nums_set = {1, 2, 3, 4, 5,'my', 6}
nums_set.discard(3)
nums_set.remove(4)  # Если элемента нет, то будет ошибка
nums_set.remove('my')
print(nums_set)

# Удаление через pop
nums_set.pop()
print(nums_set)

# Очистить множество
# num_set.clear()
# print(num_set)

# Объединение множеств
all_nums = nums_set.union(num_set)
print(all_nums)

x = {1, 2, 3}
y = {4, 5, 6, 2}
z = {7, 4, 9}
print(x | y | z)
output = x.union(y, z)      # Объединение больше двух множеств
print(output)

# нахождение совпадающих элементов

print(x & y)   # одинаковые элементы в множестве 'x' и 'y', результат: 2

# нахождение разницы между множествами

print( x - y)        # результат 1, 3
print(y - x)         # результат 4, 5, 6

# Копия множества

string_set = {'nickolas', 'jane', 1, 2, 3 ,4}
x = string_set.copy()
print(x, type(string_set))

# проверка на совпадение пересечений

name_a = {'nik', 'mike'}
name_b = {'nik', 'mick'}
y = name_b.isdisjoint(name_b)
print(y)      # Если есть совпадения, то False; если нет, то True

# Длина множества

print(len(name_b))

# frozenset

my_set = frozenset([1, 2, 3, 4])
print(my_set, type(my_set))


