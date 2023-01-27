def mean(*args):
    ls, average = [], 0
    for i in args:
        if type(i) in (int, float):
            ls.append(i)
    for j in ls:
        average = sum(ls) / len(ls)
    return average


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))