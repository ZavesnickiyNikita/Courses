from datetime import date


def saturdays_between_two_dates(start, end):
    count = 0
    if date.toordinal(end) > date.toordinal(start):
        for day in range(date.toordinal(start), date.toordinal(end) + 1):
            if date.weekday(date.fromordinal(day)) == 5:
                count += 1
        return count
    elif date.toordinal(end) < date.toordinal(start):
        for day in range(date.toordinal(end), date.toordinal(start) + 1):
            if date.weekday(date.fromordinal(day)) == 5:
                count += 1
        return count
    elif date.toordinal(end) == date.toordinal(start):
        if date.weekday(start) == 5:
            return 1
        else:
            return 0



date1 = date(2018, 7, 14)
date2 = date(2018, 7, 14)
print(saturdays_between_two_dates(date1, date2))

