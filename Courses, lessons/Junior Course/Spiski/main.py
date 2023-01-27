
def merge(n):
    sp, sp_total = [], []
    for i in range(n):
        n = input().split()
        sp.append(n)
        sp.sort()
    return sp_total

n = int(input())
print(merge(n))







