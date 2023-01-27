word1 = input().lower()
word2 = input().lower()

lst1, lst2 = [], []

for i in word1:
    lst1.append(i)

for j in word2:
    lst2.append(j)

lst1.sort()
lst2.sort()
print(True if lst1 == lst2 else False)



