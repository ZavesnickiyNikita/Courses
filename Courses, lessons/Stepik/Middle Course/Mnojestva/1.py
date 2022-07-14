
n = int(input())
a, d = [], []
b = set()
for i in range(n):
    m = input()
    a.append(m)
print(*sorted(set(a.pop()).intersection(*a)))










