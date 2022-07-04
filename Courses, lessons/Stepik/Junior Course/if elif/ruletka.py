# Программа для рулетки, где 0 зеленый, остальные поля красные либо черные
a = int(input())
if a ==0:
    print('зеленый')
elif 1 <= a <= 10:
    if a % 2 == 0:
        print('черный')
    elif a % 2 !=0:
        print('красный')
elif 11 <= a <= 18:
    if a % 2 == 0:
        print('красный')
    elif a % 2 != 0:
        print('черный')
elif 19 <= a <= 28:
    if a % 2 == 0:
        print('черный')
    elif a % 2 != 0:
        print('красный')
elif 29 <= a <= 36:
    if a % 2 == 0:
        print('красный')
    elif a % 2 != 0:
        print('черный')
elif a < 0 or a > 36:
    print('ошибка ввода')