x = input().split()
n = int(x[0])
m = int(x[1])
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
input()
y = input().split()
k = int(y[1])
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))
result = [[0] * k for i in range(n)]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in result:
    print(*i)



