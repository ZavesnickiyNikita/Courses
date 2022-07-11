# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def minus():
    result = a - b
    print(f'Результат отнимания: { result}')
    print()

def plus():
    result = a + b
    print(f'Результат сложения: { result}')
    print()

def multiplication():
    result = a * b
    print(f'Результат умножения: { result}')
    print()

def division():
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'Ошибка. На ноль делить нельзя'
    print(f'Результат деления: { result}')
    print()

def division_by_integer():
    result = a // b
    print(f'Результат деления нацело: { result}')
    print()

def remainder_of_the_division():
    result = a % b
    print(f'Результат остатка от деления: { result}')
    print()

def calculator():
    global a, b
    print('Это программа калькулятор.')
    while True:
        a = float(input('Введите число'))
        if a == 0:
            print('Выход из программы')
            break
        answer = input('Выберите операцию (+, -, *, /, //, %) ?')
        b = float(input('Введите число'))
        if answer == '+':
            plus()
        elif answer == '-':
            minus()
        elif answer == '*':
            multiplication()
        elif answer == '/':
            division()
        elif answer == '//':
            division_by_integer()
        elif answer == '%':
            remainder_of_the_division()
        else:
            print('Ошибка операции')

calculator()