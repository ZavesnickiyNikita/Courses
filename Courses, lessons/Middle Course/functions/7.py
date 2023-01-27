def print_products(*args):
    ls = []
    for i in args:
        if type(i) is str and len(i) != 0:
            ls.append(i)
    if len(ls) == 0:
        print('Нет продуктов')
    else:
        for index, value in enumerate(ls):
            print(f"{index + 1}) {value}")


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
