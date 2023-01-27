# 3.	Напишите программу, демонстрирующую работу try\except\finally.

q_1, q_2 = 140, 'smile'
try:
    q_3 = q_1 / q_2
except TypeError:
    print('Делить на строки нельзя')
finally:
    print('Исключение успешно обработано')
