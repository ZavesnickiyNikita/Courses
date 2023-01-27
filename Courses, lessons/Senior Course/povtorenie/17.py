li, total_list = [], []
n = int(input())
for i in range(n):
    li.extend(input().split(', '))

for j in li:
    if li.count(j) == n and j not in total_list:
        total_list.append(j)


if len(total_list) == 0:
    print('Сериал снять не удастся')
else:
    print(', '.join(sorted(total_list)))




