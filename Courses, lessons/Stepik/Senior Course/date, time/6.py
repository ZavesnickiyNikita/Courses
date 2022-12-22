from datetime import date


def get_date_range(start, end):
    result = []
    for day in range(date.toordinal(start), date.toordinal(end) + 1):
        result.append(date.fromordinal(day))
    return result


date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))
