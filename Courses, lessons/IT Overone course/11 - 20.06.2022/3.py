
a, b = int(input()), int(input())


try:
    c = a / b
except ZeroDivisionError:
    print('Дурачье, так нельзя')
except ValueError:
    print('Ошибка по значению')
except Exception:
    print('Какая-то ошибка, без понятия')

c = a / b
print(c)
