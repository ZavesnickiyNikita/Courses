import random
import string

length = int(input())  # длина пароля
a = string.ascii_letters + string.digits
for i in range(length):
    i = random.choice(a)
    print(i, end = '')

