from datetime import datetime, timedelta


data = input().split(' ')
list_of_dates = []
for i in data:
    list_of_dates.append(datetime.strptime(i, '%d.%m.%Y'))

result = []
for i in list_of_dates:
    result.append((i + 1) - i)
print(list_of_dates)