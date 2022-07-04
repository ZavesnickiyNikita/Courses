# Вводится 2 числа с клавиатуры (от 1 до 20).
# Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше рандомной пары.
# Проверку выполнить 7 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаев)
# вывести случайные числа, полученные в 4 итерации
import random
input_number = []       # Пустой список для введенных цифр
number_1, number_2 = int(input()), int(input())
input_number.append(number_1)
input_number.append(number_2)
print(input_number, ' Список из чисел, введенных с клавиатуры')
count_input = 0     # Счетчик для суммы введенных чисел
count_random = 0    # Счетчик для суммы генерированных чисел
list_of_random_number = []  # Список, в который добавятся все значения генерируемых чисел
attempts = 0
while attempts < 7:
    attempts += 1
    random_number = [random.randint(1, 20) for i in range(2)]
    print(f'{attempts}-я итерация рандомного списка {random_number}')
    for j in random_number:
        list_of_random_number.append(j)     # Добавляем все рандомные значения в один список
    if sum(input_number) > sum(random_number):
        count_input += 1
    if sum(random_number) > sum(input_number):
        count_random += 1
print('Кол-во раз, когда сумма введенных чисел больше рандомных: ', count_input)
print('Кол-во раз, когда сумма рандомных чисел больше введенных: ', count_random)
if count_input == count_random:
    print('Кол-во раз равно, вывод 4-й итерации рандомного списка', list_of_random_number[6:8])






