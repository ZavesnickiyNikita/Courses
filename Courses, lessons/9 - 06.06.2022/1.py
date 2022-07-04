# d = {}
# d = {'dict':1, 'dictationary':2}
# print(d)

# создание словаря с помощью команды dict()

# e = dict(short = 'dict', long = 'dictationary')
# e_2 = dict([(1, 1), (2, 4)])
# print(e, '\n', e_2)

# метрод fromkeys создает словарь только с ключами или одинаковыки значениями

# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)

# Создание словаря с помощью генератора словарей

# d = {a: a ** 2 for a in range(7)}
# print(d)

# Добавление элемента в словарь
d = {1: 2, 2: 4, 3: 9}
d[4] = 4 ** 2

print(d[1])         # [1] это ключ, а не индекс
print(d)

