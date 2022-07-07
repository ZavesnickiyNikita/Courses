import math
def square(n):
    p = n * 4
    s = n ** 2
    diag = math.sqrt(n ** 2 + n ** 2)
    return p, s, diag

n = int(input())
print(square(n))
