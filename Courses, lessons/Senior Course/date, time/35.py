from datetime import *

time = input()
time = datetime.strptime(time, '%H:%M:%S')
n = timedelta(seconds=int(input()))
new_time = time + n

print(new_time.time())