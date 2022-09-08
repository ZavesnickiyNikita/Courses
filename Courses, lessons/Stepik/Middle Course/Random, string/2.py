import random
import string

a = int
total = []
sp = string.digits
sp = sp[1:]
while True:
    a = random.sample(sp, 7)
    if a not in total:
        total.append(a)
        if len(total) == 100:
            break

for i in total:
    print(*i, end = '\n', sep = '')







