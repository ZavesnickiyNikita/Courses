li = [int(i) for i in input().split()]
print(*sorted(filter(lambda x: li.count(x) > 1, set(li))))