li = [i for i in range(1, int(input()) + 1)]
result = []
total = []
for i in li:
    s = sum(map(int, list(str(i))))
    result.append(s)
for j in result:
    total.append(result.count(j))
print(max(total))


