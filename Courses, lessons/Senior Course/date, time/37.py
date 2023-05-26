from datetime import datetime, timedelta


data = input()
result = []
current_date = datetime.strptime(data, '%d.%m.%Y')
for i in range(2, 12):
    result.append(current_date.date())
    current_date = current_date + timedelta(days=i)
for j in result:
    print(j.strftime('%d.%m.%Y'))



