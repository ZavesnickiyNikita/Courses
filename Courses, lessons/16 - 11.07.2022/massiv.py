import random
def massiv():
    n, m = int(input()), int(input())
    a = [random.randint(n, m) for i in range(10)]
    print(a)

massiv()

