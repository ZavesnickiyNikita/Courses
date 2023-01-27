def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for keys, values in sorted(kwargs.items()):
        print(keys, values, type(values))


print_given(1, [1, 2, 3], 'three', two=2)