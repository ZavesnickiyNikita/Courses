def spell(*args):
    dct, lenght = {}, 0
    for i in args:
        dct.setdefault(str(i).lower()[0], 0)
    for i in args:
        dct.update(i)
    return dct


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))