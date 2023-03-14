from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, minutes=60*12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))