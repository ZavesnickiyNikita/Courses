
def find_something():
    a, b = (), []
    answer = input('Что вы хотите создать? Кортеж или список?').lower()
    if answer == 'кортеж':
        lst_str = []
        a = (101, 222, 333, 'У Вас была какая-то тактика и вы её придерживались?',
             ' У меня была какая-то тактика и я её придерживался!')
        print(a, ' <------ Кортеж для примера')
        for i in a:
            if type(i) is str:
                lst_str.append(i)
        lst_str = ''.join(lst_str)
        lst_str = lst_str.split()
        len_words = 0
        for j in lst_str:
            len_words += len(j)
        print(f'Длина слов в массиве равна: {len_words}')
    elif answer == 'список':
        b = [101, 222, 333, 24, 31, 7, 4, 1024, 'У Вас была какая-то тактика и вы её придерживались',
             ' У меня была какая-то тактика и я её придерживался']
        print(b, '<------ Список для примера')
        list_numbers, list_letters = [], []
        for k in b:
            if type(k) is int:
                list_numbers.append(k)
            elif type(k) is str:
                list_letters.append(k)
        count1, count2 = 0, 0
        for i in list_numbers:
            count1 += 1
        print('Количество цифр в списке:', count1)
        count3 = 0
        for i in list_numbers:
            if i % 2 != 0:
                count3 += 1
        print('Количество нечетных чисел', count3)
        c = []
        for i in list_letters:
            for j in i.lower():
                if j in 'ёйфяцычувскамепинртгоьшлбщдзжхэъ':
                    c.append(j)
        print('Количество букв в строке', len(c))

find_something()