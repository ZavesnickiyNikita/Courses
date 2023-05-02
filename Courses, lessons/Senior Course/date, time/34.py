from datetime import *


time = input()
time = datetime.strptime(time, '%H:%M:%S')
next_day = time + timedelta(days=1)

print(next_day - (next_day - time))


