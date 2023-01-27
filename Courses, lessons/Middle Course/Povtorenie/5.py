n = 8
xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[y][x] = 'Q'
        if abs(y - i) == abs(x - j) or y == i or x == j:
            a[i][j] = '*'

for i in a:
    print(*i)