

while True:
    a = input('Введите значение "a"')
    b = input('Введите второе значение "b"')
    try:
        c = int(a) / int(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('Доступны только числа')
    else:
        print('a / b = ', c)
        break













