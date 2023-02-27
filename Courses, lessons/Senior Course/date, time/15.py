from datetime import date



# def print_good_dates(dates):
#     result = []
#     for day in dates:
#         if day.strftime('%Y') == '1992' and (int(day.strftime('%m')) + int(day.strftime('%d'))) == 29:
#             result.append(day)
#         else:
#             pass
#     result = sorted(result)
    
#     for day in result:
#         print(day.strftime('%B %d, %Y'))



def print_good_dates(dates):
    for i in sorted(filter(lambda x: x.year == 1992 and x.month + x.day == 29, dates)):
        print(i.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)