
import random
n = int(input('Кол-во строк: '))
m = int(input('Кол-во столбцов: '))
a = [[0] * m for i in range(n)]c
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(1, 100)
        print(a[i][j], end = ' ')
    print()
item = int(input())
for i in range(n):
    if item in a[i]:
        print('Строка(index): ', i)
print()

for j in range(m):
    for i in range(n):
        if a[i][j] == item:
            print('Колонка (index):', j)
print()
