#  Секунды в дни : минуты : часы
def time(seconds):
    days = seconds // 86400
    seconds -= days * 86400
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    print(f'Дни {days}: часы {hours}: минуты{minutes}: секунды{seconds}')


seconds = int(input('Введите кол-во секунд'))
time(seconds)



