athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
            ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
            ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def name(num):
    return num[0]

def age(num):
    return num[1]

def growth(num):
    return num[2]

def weight(num):
    return num[3]


slovar = {1: name, 2: age, 3: growth, 4: weight}
athletes.sort(key=slovar.get(int(input())))
for i in athletes:
    print(*i)