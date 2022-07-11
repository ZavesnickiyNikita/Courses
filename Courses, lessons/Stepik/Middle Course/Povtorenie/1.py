x = input().split()
n = int(x[0])
m = int(x[1])
a = [[0] * m for i in range(n)]
b = [[0] * m for i in range(n)]
nm = 0
for i in range(n):
    for j in range(m):
        a[i][j] = 78
for i in range(n):
    for j in range(m):
        print(str(b[i][j]).ljust(3), end = ' ')
    print()

for i in range(n):
    for j in range(m):
        b[i][j] = 4
for i in range(n):
    for j in range(m):
        print(str(b[i][j]).ljust(3), end = ' ')
    print()















