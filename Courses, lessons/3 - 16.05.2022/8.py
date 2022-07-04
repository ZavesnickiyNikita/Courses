arr = ['гречка', 'картошка', 'макароны', 'суп', 'рис']
print(arr)
a = input('Что ты не любишь?')
for i in arr:
    if i == a:
        print(i + ' Это не ем')
        continue
    else:
        print(i + ' Это ем')