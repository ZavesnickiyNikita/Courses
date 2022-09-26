lst = []
for i in range(int(input())):
    a = input()
    lst.append(a)

print(*sorted(lst, key=lambda x: sum([int(item) * (256**(3 - index)) for index, item in enumerate(x.split('.'))])), sep='\n')