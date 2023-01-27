
with open('zadacha1.txt') as a:
    b = a.readlines()
for i in b:
    i = i.replace('_', ' ')
    c = i.split()
print(c)

d = 0
for j in c:
    if j.isdigit():
        j = int(j)
        d += j
print(d)
