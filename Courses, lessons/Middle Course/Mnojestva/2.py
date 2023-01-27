
a = input().split()
b = input().split()
c = input().split()
a1, b1, c1 = [], [], []
for i in a:
    i = int(i)
    a1.append(i)
for j in b:
    j = int(j)
    b1.append(j)
for k in c:
    k = int(k)
    c1.append(k)
a1, b1, c1 = set(a1), set(b1), set(c1)
d1 = set(range(0, 11))
e1 = d1.difference(a1 | b1 | c1)
print(*sorted(e1))

