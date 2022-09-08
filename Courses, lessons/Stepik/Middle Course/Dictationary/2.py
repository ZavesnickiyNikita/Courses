n = int(input())
sp = []
a1, a2, a3 = [], [], []
d1, total_dict = {}, {}
for i in range(n):
    a = input().split()
    a1, a2, a3 = a[0], a[1], int(a[2])
    if a1 not in d1.keys():
        d1[a1] = d1.setdefault(a1, {a2: a3})
    else:
        if a2 not in d1[a1]:
            d1[a1].update({a2: a3})
        else:
            d1[a1][a2] =d1[a1].get(a2) + a3

for name, purchase in sorted(d1.items()):
    print(name + ':')
    for product in sorted(purchase):
        print(product, purchase[product])




