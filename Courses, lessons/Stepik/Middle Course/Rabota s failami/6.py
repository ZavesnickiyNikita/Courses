import re

with open('nums.txt', 'r', encoding='utf-8') as file:
    sp = [re.findall('\d+', i) for i in file.readlines()]
    summ = 0
    for i in sp:
        for j in i:
            summ += int(j)
    print(summ)





