#  Есть массив состоящий из слов и чисел, нужно записать в файл сначала
#  слова в порядке их длины, а после слов цифры в порядке возрастания.

file = open('DZ#12.txt', 'w')       # Создаем файл
b_letters, b_numbers = [], []
a = (123, 23, 14, 94, 85, 'magazine', 'newspaper', 'book', 6, 37, 'journal', 'Washington Post', 'Komsomolka')
for i in a:
    if type(i) is str:              # Если i - строка, в список со строками
        b_letters.append(i)
    elif type(i) is int:            # Если i - число, в список с числами
        b_numbers.append(i)
b_letters = sorted(b_letters, key = len)    # Сортируем по длине
b_numbers = sorted(b_numbers)               # Сортируем по возрастанию
for j in b_letters:
    file.write(j + ', ')                    # Записываем строки через запятую
file.write('\n')                            # Перенос на след строку
for k in b_numbers:
    file.write(str(k) + ', ')               # Записываем числа через запятую
file.close()                          # Закрываем файл в режиме записи

file = open('DZ#12.txt', 'r')       # открываем в режиме чтения
print(*file)                        # Выводим содержимое
file.close()





