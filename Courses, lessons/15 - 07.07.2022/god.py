def visokosnii_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

year = int(input('Введите год '))
print(visokosnii_year(year))