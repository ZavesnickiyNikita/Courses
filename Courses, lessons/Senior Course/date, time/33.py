from datetime import *

date = input()
date = datetime.strptime(date, '%d.%m.%Y')

next_date = date + timedelta(days=1)
previous_date = date - timedelta(days=1)

print(previous_date.strftime('%d.%m.%Y'))
print(next_date.strftime('%d.%m.%Y'))