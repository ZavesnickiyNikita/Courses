## Обработка ошибок
# try:
#     a = 100 / 0
# except BaseException:
#     a = 'Ты дурак, так нельзя'
# print(a)


# my_dict = {'a':1, 'b': 2, 'c': 3}

# try:
#     value = my_dict['d']
# except KeyError:
#     print('Ключа не существует')

# my_list = [1, 2, 3, 4, 5, 6]
# try:
#     my_list[6]
# except IndexError:
#     print('Этого индекса нет в списке')

# my_dict = {'a':1, 'b': 2, 'c': 3}

# try:
#     value = my_dict['d']
# except IndexError:
#     print('Ошибка по индексу')
# except KeyError:
#     print('Такого ключа нет')
# except:
#     print('Другая ошибка')

# Оператор finally - выполняется в любом случае

# my_dict = {'a':1, 'b': 2, 'c': 3}
#
# try:
#     value = my_dict['d']
# except IndexError:
#     print('Ошибка по индексу')
# except KeyError:
#     print('Вы самое слабое звено - прощайте')
# else:
#     print('Шансов мало, но что-то есть')
# finally:
#     print('Ты не дурак, шансы есть')

