word = input()
num = int(input())
ls, result = [], []
ls_word = []

for index, letter in enumerate(word):
    if letter in 'ауоыиэяюёе':
        ls_word.append(index)

for i in range(num):
    words = input()
    for index, letter in enumerate(words):
        if letter in 'ауоыиэяюёе':
            ls.append(index)
    if ls_word == ls:
        result.append(words)
    ls = []


print(*result, sep='\n')
