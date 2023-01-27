from functools import reduce


def pretty_print(data, side='-', delimiter='|'):
    s = f' {delimiter} '.join(map(str, data))
    s = f'{delimiter} {s} {delimiter} '
    print(' ' + side * (len(s) - 3))
    print(s)
    print(' ' + side * (len(s) - 3))


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

