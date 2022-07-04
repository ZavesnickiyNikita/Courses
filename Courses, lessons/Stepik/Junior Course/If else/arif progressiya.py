# Напишите программу, которая определяет, являются ли три заданных числа
# (в указанном порядке) последовательными членами арифметической прогрессии.
number1 = int(input())
number2 = int(input())
number3 = int(input())
if number3 - (number2 - number1) == number2  or number1 - (number2 - number3) == number2:
    print('Yes')
else:
    print('No')

