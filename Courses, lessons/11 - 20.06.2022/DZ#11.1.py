# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.
import random
line = 5
column = 5
matrix = [[0] * column for i in range(line)]
for i in range(line):
    for j in range(column):
        matrix[i][j] = random.randint(1, 101)
print(*matrix, sep ='\n')
max_sum_line = -1
index_max_sum_line = -1
for i, j in enumerate(matrix):
    if sum(j) > max_sum_line:
        max_sum_line = sum(j)
        index_max_sum_line = i
print('----------------------')
print('Индекс строки с максимальной суммой элементов: ', index_max_sum_line)
print()

# Второй способ


line = 5
column = 5
matrix = [[0] * column for i in range(line)]
for i in range(line):
    for j in range(column):
        matrix[i][j] = random.randint(1, 101)
print(*matrix, sep ='\n')
print('----------------------')
s = []
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print('Строка с максимальными значениями: ', matrix[s.index(max(s))])
print('Индекс данной строки: ',[s.index(max(s))])









