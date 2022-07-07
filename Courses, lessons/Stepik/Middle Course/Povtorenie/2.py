
n = int(input())
a = []
count = 0
sum_i, sum_j, sum_gl, sum_pb = [], [], [], []
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in a:
    sum_i.append(sum(i))
for i in range(len(a)):
    e = 0
    for j in range(len(a)):
        e += a[j][i]
    sum_j.append(e)
for i in range(n):
    sum_gl.append(a[i][i])
    sum_pb.append(a[i][n - i - 1])
r = sum(sum_gl)
t = sum(sum_pb)
st_sum_i = set(sum_i)
st_sum_j = set(sum_j)
total = []
for i in range(n):
    for j in range(n):
        total.append(a[i][j])
count_2 = 0
for i in range(1, n ** 2 + 1):
    if i in total:
        count_2 += 1
    else:
        count_2 = 0
count_3 = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            count_3 = 1
        else:
            count_3 = 0
if r == t and count_3 == 1 and count_2 == n ** 2 and len(st_sum_i) == 1 and len(st_sum_j) == 1:
    print('YES')
else:
    print('NO')



























