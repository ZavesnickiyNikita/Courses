from datetime import date


data_list = []
for _ in range(int(input())):
    data = date.fromisoformat(input())
    data_list.append(data)

# print(*sorted(map(lambda x: x.strftime('%d/%m/%Y'), data_list)), sep='\n')
result = sorted(data_list)

for i in result:
    print(i.strftime('%d/%m/%Y'))

