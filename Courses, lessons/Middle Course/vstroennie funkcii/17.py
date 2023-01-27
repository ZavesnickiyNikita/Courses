a = int(input())
b = int(input())

total_lst = []
for i in range(a, b + 1):
    d = []
    while i != 0:
        d.append(i % 10)
        i = i // 10
        if all(map(lambda j: i % j == 0, d)):
            total_lst.append(i)

print(total_lst)

