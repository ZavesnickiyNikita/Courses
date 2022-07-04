# Пребразовать текст в список слов с удалением знаков препинания

words = input()
listen = ''
puncuations = '.,'
for i in words:
    if i not in puncuations:
        listen += i
print(listen)