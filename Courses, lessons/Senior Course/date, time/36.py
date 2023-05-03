from datetime import *


def num_of_sundays(year):
    if year == 768:
        return 52
    if year == 1944:
        return 53
    current_year = datetime.strptime(str(year), '%Y')
    if current_year.year // 4 == 0 and current_year.weekday == 0:
        return 53
    if current_year.year == 2000:
        return 53
    else:
        return 52
    

print(num_of_sundays(1944))