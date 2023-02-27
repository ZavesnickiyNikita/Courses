from datetime import date


count = 0
while True:
    data = input()
    if data == 'end':
        break
    else:
        try: 
            year, month, day = data.split('.')   
            check = date(int(day), int(month), int(year))
            print('Корректная')
            count += 1
        except ValueError:
            print('Некорректная')

print(count)


