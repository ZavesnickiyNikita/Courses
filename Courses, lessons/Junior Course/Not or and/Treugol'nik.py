# Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.
ab, bc, ac = int(input()), int(input()), int(input())
if ab < bc + ac and bc < ab + ac and ac < ab + bc:
    print('YES')
else:
    print('NO')
