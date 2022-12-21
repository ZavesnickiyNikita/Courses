from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
result = []

for day in dates:
    if day.month in (1, 2, 3):
        result.append(f"{day.year}-Q1")
    elif day.month in (4, 5, 6):
        result.append(f"{day.year}-Q2")
    elif day.month in (7, 8, 9):
        result.append(f"{day.year}-Q3")
    elif day.month in (10, 11, 12):
        result.append(f"{day.year}-Q4")


print(*result, sep="\n")