a, b = input(), input()
if a == 'красный':
    if b == 'синий':
        print('фиолетовый')
    elif b == 'желтый':
        print('оранжевый')
    elif b == 'красный':
        print('красный')
    else:
        print('ошибка цвета')
elif a == 'синий':
    if b == 'красный':
        print('фиолетовый')
    elif b == 'желтый':
        print('зеленый')
    elif b == 'синий':
        print('синий')
    else:
        print('ошибка цвета')
elif a == 'желтый':
    if b == 'красный':
        print('оранжевый')
    elif b == 'синий':
        print('зеленый')
    elif b == 'желтый':
        print('желтый')
    else:
        print('ошибка цвета')
elif a != 'красный':
        print('ошибка цвета')
elif a != 'синий':
        print('ошибка цвета')
elif a != 'желтый':
        print('ошибка цвета')

