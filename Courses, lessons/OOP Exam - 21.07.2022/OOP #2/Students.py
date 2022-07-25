import random

class Students:

    def __init__(self, name, money):
        self.name = name
        self.money = money

student1 = Students('Сергей', random.randrange(100, 1000))
student2 = Students('Максим', random.randrange(100, 1000))
student3 = Students('Гриша', random.randrange(100, 1000))
student4 = Students('Дима', random.randrange(100, 1000))
student5 = Students('Иван', random.randrange(100, 1000))
student6 = Students('Игорь', random.randrange(100, 1000))
student7 = Students('Стас', random.randrange(100, 1000))
student8 = Students('Леша', random.randrange(100, 1000))

total_sdudents = [student1, student2, student3, student4, student5, student6, student7, student8]

total_money = []
for i in total_sdudents:
    total_money.append(i.money)

if min(total_money) == max(total_money):
    print('У Всех одинаковое количество денег')

maxx = 0
for j in total_sdudents:
    if j.money >= maxx:
        maxx = j.money
        name = j.name

print(f'Максимальная сумма {maxx} рубля у студента {name}')