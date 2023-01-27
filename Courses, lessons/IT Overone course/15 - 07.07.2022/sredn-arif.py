import random
n = int(input())
def sredn_arifm(n):
    s = 0
    sr = 0
    a = [random.randint(1, 10) for i in range(n)]
    print(a)
    for j in a:
        s += j
    sr = s / n
    return sr


print(sredn_arifm(n))