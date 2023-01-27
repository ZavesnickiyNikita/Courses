while True:
    a = float(input('Введите первое число: '))
    operator = input('Введите операцию: ')
    b = float(input('Введите второе число: '))

    if operator == '+':
        c = a + b
        print(c)
        break
    elif operator == '-':
        c = a - b
        print(c)
        break
    elif operator == '*':
        c = a * b
        print(c)
        break
    elif operator == '/':
        if b == 0:
            print('На ноль делить нельзя')
        elif b != 0:
            c = a / b
            print(c)
        break