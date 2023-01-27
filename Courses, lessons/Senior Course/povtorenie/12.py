d1 = int(input())
d2 = int(input())
d3 = int(input())
first = d1 + d2 + d3
li = []
li.append(d1)
li.append(d2)
li.append(d3)
minn = min(li)
maxx = max(li)
li.remove(maxx)
li.remove(minn)
average = li[0]
second = minn * 2 + average * 2
print(min(first, second))
