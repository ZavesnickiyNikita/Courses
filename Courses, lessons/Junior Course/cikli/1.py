name = input()
count = 0
for i in range(len(name)):
    if name[i] in '0123456789':
        count += 1
if count > 0:
    print('Цифра')
else:
    print('Цифр нет')










