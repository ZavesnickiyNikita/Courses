
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            a[i][j] = max(i, j) - min(i, j)
for i in a:
    print(*i)