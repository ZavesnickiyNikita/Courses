# elements = []
# elements.append('a')
# elements.append(1)          # добавление элементов в конец списка
#
# print(elements)


# elements = [1, 3, 'a', 6, 'b']          # добавление элемента на указаную позицию
# elements.insert(1, 2)                   # без удаления элементов
# print(elements)

# elements = [1, 3, 'a', 6, 'b']
# elements[1] = 2                       # изменение элементов списка с удалением замененного элемента
# print(elements)                      # [1] номер позиции в списке, 2 сам добавленный элемент


# elements = [1, 3, 'a', 6, 'b']
# del elements[1]                              # удаляет элемент по индексу (порядковому номеру)
# print(elements)
#
# elements = [1, 3, 'a', 6, 'b', 'a']
# elements.remove('a')                        # удаляет элемент по его значению
# print(elements)                             # только одно первое значение
#
#
# my_list = ['hello', 'world']
# elements = [1,3, my_list, 6, 'a', 'b']
#
# del elements [2][1]             # [2] индекс основного списка, [1] индекс вложенного списка
# print(elements)

# del elements[4:]     # удаляем все элементы после 4-го элемента ( включительно)
# print(elements)

# del elements[:2]  # удаляем все элементы до 2-го элемента
# print(elements)

# del elements[1:3]   # удаляем от 1-го элемента до 3-го элемента
# print(elements)
#
# elements = [1, 3, 6, 'a', 'abc', 123, 435]
#
# if 3 in elements:
#     print('есть такой')          # проверяем наличие элемента в списке
# else:
#     print('такого нет')
#
# a = ['a', 5, 2, 3, 6]
# b = [1, 2, 3]               # оператором "+" получаем новый список
# # print(a + b)
#
# a.extend(b)             # при сложении командой extend добавляем список (б) к списку (а)
# print(a)
#
# #  скопировать список
#
# a = [1, 2, 3, 4]
# b = a           # переменной b присваивается не значение списка, а его адрес
# a.append(5)
# b.append(6)
# print('a', a, 'b', b)
# #
# a = [1, 2, 3]
# b = a.copy()
# print(id(a), id(b), a, b)      # id - уникальный номер объекта, который хранится в ячейке памяти
# a.append(4)                    # командой copy переменная не принимает новые значения
# b.append(5)                    # скопированная переменная остается неизменяемой
# print(a, b)
#
#  Циклы по спискам
# elements = [1, 2, 3, 'meow']
# for i in elements:                   # чтобы перебрать целый список, удобнее использовать for
#     print(i)
#
# elements = [1, 2, 3, 'meow']
# elements_len = len(elements)        # определяем длину списка, добавить переменную i = 0
# i = 0
# while i < elements_len:
#     print(elements[i])
#     i += 1
#
# #  clear
# a = [1, 2, 3]
# a.clear()          # Удаляет все эл-ты списка
# print(a)
#
#  count
# elements = ['one', 'two', 'three', 'one', 'two', 'one']
# print(elements.count('one'))            # подсчитывает количество элементов в списке

#  index
# elements = ['one', 'two', 'three', 'one', 'two', 'one']
# print(elements.index('three'))             # выводит индекс нужного нам элемента
#
# pop
# elements = [1, 'meow', 3, 'meow']
# # print(elements)
# b = elements.pop(1)             # удаляет элемент с индексом [1]
# print(b ,elements)
#
# reverse
# a = [1, 2, 3, 4, 5, 6]
# a.reverse()
# print(a)
#
# sort (по возрастанию)
# elements = [3, 19, 20, 100, 0, 5]
# elements.sort()                             # сортируем список по убыванию либо возрастанию
# print(elements)
# #
# #  sort ( по убыванию)
# elements = [3, 19, 20, 100, 0, 5]
# elements.sort( reverse = True)
# print(elements)
# #
# #  Вложенные списки
#
# elements = [['яблоки', 50], ['апельсины', 190], ['груши', 100]]
# print(elements[0])
#
# print(elements[1][1])
#
# # Срезы
#
# elements = [0.1, 0.2, 1, 2, 3, 4, 0.3, 0.4]
# int_elements = elements[2:6]
# print(elements, int_elements)
