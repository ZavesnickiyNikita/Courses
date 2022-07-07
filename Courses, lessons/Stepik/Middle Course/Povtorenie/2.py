
n = int(input())
a = []
count = 0
sum_i, sum_j, sum_gl, sum_pb = 0, 0, 0, 0
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] != 0 and (a[i][j] ):
            sum_i += a[i][j]
            sum_j += a[j][i]
            sum_gl += a[i][i]
            sum_pb += a[i][n - i - 1]
            if sum_i == sum_j == sum_gl == sum_pb:
                    count += 1
            else:
                count = 0
        else:
            break
if count == 1:
    print('YES')
else:
    print('NO')


























