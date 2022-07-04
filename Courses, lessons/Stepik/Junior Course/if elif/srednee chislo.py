# Даны три различных целых числа. Напишите программу, которая находит
# среднее по величине число.
a = int(input())
b = int(input())
c = int(input())
if a < b < c or a > b > c:
    print(b)
elif b < a < c or b > a > c:
    print(a)
elif a < c < b or a > c > b:
    print(c)
