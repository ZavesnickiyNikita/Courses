def greet(name, *args):
    ls, a = [], ''
    if len(args) == 0:
        return f'Hello, {name}!'
    if len(args) > 0:
        ls.append(name)
        for i in args:
            ls.append(f' and {i}')
        for j in ls:
            a += j
        return f'Hello, {a}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))