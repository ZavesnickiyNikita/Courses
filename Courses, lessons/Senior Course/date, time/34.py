from datetime import *


time = input()
time = datetime.strptime(time, '%H:%M:%S')

previous_day = '00:00:00'
previous_day = datetime.strptime(previous_day, '%H:%M:%S')

total_seconds = timedelta.total_seconds(time - previous_day)
print(str(total_seconds)[:-2])