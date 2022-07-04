def is_valid(n):
    if n in range(1, 100):
        pass
    else:
        print('А может быть все-таки введем целое число в границах загаданного?)')


import random
def find_number(n):
    print('Я загадаю число')
    print('Введи границы. Например, если от 1 до 100, то число 105 я загадать не смогу')
    a1, a2 = int(input('Укажите начальную границу')), int(input('Укажите конечную границу'))
    num = random.randint(a1, a2)
    print('Я загадал число. Угадай его!')
    count = 0
    while True:
        try:
            n = int(input('Введите число'))
        except ValueError:
            print('Только Числа!')
            n = int(input('Введите число'))
        if n > a2:
            is_valid(n)
        if n > num and n <= a2:
            print('Слишком много.\n'
                  'Попробуйте еще раз')
            count += 1
        elif n < num and n >= a1:
            print('Слишком мало.\n'
                  'Попробуйте еще раз')
            count += 1
        elif n == num:
            count += 1
            print('Вы угадали, поздравляем!')
            print(f'Вам понадобилось {count} попыток, вы молодец!')
            print('------------------------')
            break

while True:
    print('Приветсвую Вас на игре угадай число:)')
    print('Вы готовы начать играть?')
    n = input('да/нет').lower()
    if n == 'да':
        find_number(n)
    elif n == 'нет':
        print('Вы точно уверены?) Начнем игру?)')
        n = input().lower()
        if n == 'да':
            find_number(n)
        else:
            print('Очень жаль, с нетерпением ждем Вас!')
            break

