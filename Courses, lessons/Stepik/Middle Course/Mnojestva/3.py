m = int(input())
list1 = []
set1 = set()

for i in range(m):
    n = int(input())
    for j in range(n):
        l = input()
        list1.append(l)

for i in list1:
    if list1.count(i) == m:
        set1.add(i)

print(*sorted(set1), sep = '\n')






