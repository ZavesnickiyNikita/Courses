#  Рекурсивная функция

# def factorial(n):
#     if n != 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
#
# print(factorial(5))

# Переименование функции переменной

# def add(a, b):
#     return a + b
#
# variable = add(2, 3)
# print(variable)

# Присвоение функции переменной

# def func(x): return x
#
# apple = func
# print(apple(5))

# Лямбда функция
# product = lambda x, y: x * y
# print(product(2, 3))

# Функция внутри функции

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(mul(3)(4))

# Декоратор функции. Старый вариант

# def simple_decore(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return wrapper
#
# def first_test():
#     print('Test function 1')
#
# def second_test():
#     print('Test function 2')
#
# first_test_wrapped = simple_decore(first_test)
# second_test_wrapped = simple_decore(second_test)
# first_test_wrapped()
# second_test_wrapped()

# Декоратор функции. Новый вариант

def simple_decore(fn):
    def wrapper():
        print('Start function')
        fn()
        print('Stop function')
    return wrapper

@simple_decore
def fist_test():
    print('Test fuction 1')

@simple_decore
def second_test():
    print('Test fuction 2')

fist_test()
second_test()