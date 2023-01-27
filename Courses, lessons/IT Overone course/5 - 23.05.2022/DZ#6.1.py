# Дан список. Все числа этого списка проверить на четность. Если число четное,
# то посчитать сумму его цифр. Если нечетное, то заменить его на 1 в списке.
# Все слова: посчитать количество гласных и согласных. Все вывести на экран
vowels = 0
consonants = 0
list = [15, 48, 'hello', 6, 19, 'world', 19, 23, 36, 30, 'school', 'midnight']
for i in list:
    if type(i) is int:
        if i % 2 == 0:
            s1 = i // 10  # первая цифра четного числа
            s2 = i % 10  # вторая цифра четного числа
            s = s1 + s2
            print('Сумма цифр числа', i , 'равна: ', s)
        else:
            index = list.index(i)
            list[index] = 1
    elif type(i) is str:
        for j in i:
            if j in 'aeyuio':
                vowels += 1
            else:
                consonants += 1
print(list)
print('Количество гласных равно: ', vowels)
print('Количество согласных равно: ', consonants)













