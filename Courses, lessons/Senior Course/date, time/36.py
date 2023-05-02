from datetime import *


def num_of_sundays(year):
    year = datetime.year(year)
    return year // 7


print(num_of_sundays(2021))