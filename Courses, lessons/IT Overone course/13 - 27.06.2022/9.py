# 12.	Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’
#  их разность
a = open('input.txt', 'w')
q1, q2 = 10, 5
a.write(str(q1) + ' ' + str(q2) + '\n')
b = q1 - q2
a.write(str(b))
a.close()

c = open('output.txt', 'w')
c.write(str(b))
c.close()