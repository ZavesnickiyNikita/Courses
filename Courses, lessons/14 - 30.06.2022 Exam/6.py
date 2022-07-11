# 6.	Ввести 10 чисел, данные числа добавить их во множество.
list_1 = []
n = '1 2 3 4 5 6 7 8 9 10'
for i in n.split():
    i = int(i)
    list_1.append(i)
list_2 = tuple(list_1)
print(list_2)