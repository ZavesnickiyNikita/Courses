from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = timedelta.total_seconds(today - birthday) // 86400

print(days)