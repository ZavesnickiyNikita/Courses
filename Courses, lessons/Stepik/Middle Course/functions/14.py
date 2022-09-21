number = input().split()
number.sort(key=int)


def comparator(num):
    a = int()
    for i in num:
        a += int(i)
    return a


print(*sorted(number, key=comparator))
