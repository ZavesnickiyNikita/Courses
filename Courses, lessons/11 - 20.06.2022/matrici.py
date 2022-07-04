# Создание матриц
# n = 3
# m = 2
# a = []                  # m - строки
# for i in range(n):      # n - столбцы
#     a.append([0] * m)
# print(a)

# Создание матриц с помощью генератора
# n = 3
# m = 2
# a = [[2] * m for i in range(n)]
# print(a)


# a = [[1, 4, 5, 12],
#      [-5, 8, 9, 0],
#      [-6, 7, 11, 19]]
# print('a =', a)          # вся матрица
# print('a[1] =', a[1])    # вторая строка
# print('a[1][1] =', a[1][1])        # вторая строка, второй элемент
# print('a[2][-1]', a[2][-1])        # третья строка, последний эл-нт
#
# column = []
# for i in a:
#      column.append(i[2])           # вывод 3-го столбца из матрицы
# print('3d column', column)

#  Вывод списка из матрицы
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#      for j in range(len(a[i])):
#           print(a[i][j], end = '')
#      print()

#  Заполнение матрицы
import random
n = 4
m = 5
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(1, 101)
print(a)
