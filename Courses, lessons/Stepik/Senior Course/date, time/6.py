from datetime import date
from random import *


def get_date_range(start, end):
    result = []
    for day in range(start, end):
        result.append(day)
    return result


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')
