n = int(input())
count_1, count_2, count_3, count_4 = 0, 0, 0, 0
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
v = ((1 + n) / 2) * n
for i in range(n):
    if sum(a[i]) == v:
        count_3 += 1
    for j in range(n):
        if 1 <= a[i][j] <= n:
            b.append(a[i][j])
    c = set(b)
    if len(c) == n:
        count_1 += 1
    else:
        count_1 -= 1
f = []
e = [list(reversed(i)) for i in zip(*a)]
for i in range(n):
    if sum(e[i]) == v:
        count_4 += 1
    for j in range(n):
        if 1 <= e[i][j] <= n:
            f.append(e[i][j])
    d = set(b)
    if len(d) == n:
        count_2 += 1
    else:
        count_2 -= 1
if count_1 == n and count_2 == n and count_3 == n and count_4 == n:
    print('YES')
else:
    print('NO')






