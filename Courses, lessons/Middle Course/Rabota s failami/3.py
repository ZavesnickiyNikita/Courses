
file = open('prices.txt', 'r', encoding='utf-8')

summa = 0
for i in file.readlines():
    arr = i.split()
    summa += int(arr[1]) * int(arr[2])

print(summa)


file.close()