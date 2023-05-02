from datetime import *


def num_of_sundays(year):
    current_year = datetime.strptime(str(year), '%Y')
    next_year = current_year + date.year(1)
    return next_year
    # count = 0
    # for i in range(current_year):
    #     if i == datetime.weekday(6):
    #         count += 1
    # return count
    

print(num_of_sundays(2021))