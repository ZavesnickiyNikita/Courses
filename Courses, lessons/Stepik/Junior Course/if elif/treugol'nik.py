# Напишите программу, которая принимает три положительных числа и определяет
# вид треугольника, длины сторон которого равны введенным числам.
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a == c != b or b == c != a:
    print('Равнобедренный')
else:
    print('Разносторонний')