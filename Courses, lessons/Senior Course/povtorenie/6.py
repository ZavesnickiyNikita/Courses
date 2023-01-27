def filter_anagrams(word, words):
    dct, dct2, lst = {}, {}, []
    for i in word:
        dct.setdefault(i, word.count(i))
    for i in words:
        for j in i:
            dct2.setdefault(j, i.count(j))
        if dct == dct2:
            lst.append(i)
        dct2 = {}
    return lst


print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))