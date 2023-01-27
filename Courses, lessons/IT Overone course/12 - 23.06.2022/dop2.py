#  В текстовом файле посчитать количество строк, а также для каждой отдельной строки
#  определить количество в ней символов.
import os
a = open('123.txt', 'w')
while True:
    b = input('Введите значение')
    if len(b) == 0:
        break
    a.write(b + '\n')
a.close()

c = open('123.txt')
count_lines = 0
count_symblos = 0
for i in c:
    count_lines += 1
    print(i, len(i) - 1,'Кол-во символов в строке')
print(f'{count_lines} - кол-во строк в файле')
c.close()




