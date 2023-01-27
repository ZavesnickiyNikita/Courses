from fractions import Fraction as F
from math import *


sp = []
m = int(input())
for i in range(1, m + 1):
    for j in range(1, m + 1):
        if 0 < F(i, j) < 1:
            sp.append(F(i, j))
sp.sort()
sp = set(sp)
sp = list(sp)
sp.sort()
print(*sp, sep = '\n')








