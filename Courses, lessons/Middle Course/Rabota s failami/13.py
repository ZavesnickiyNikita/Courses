with open('logfile.txt', 'r', encoding='utf-8') as logfile, open('output.txt', 'w', encoding='utf-8') as output:
    lst = []
    for i in logfile.read().split('\n'):
        name = i.split(',')[0]
        time_in = i.split(',')[1]
        time_off = i.split(',')[-1]
        if ((int(time_off.split(':')[0]) * 60) + (int(time_off.split(':')[1]))) -\
            ((int(time_in.split(':')[0]) * 60) + (int(time_in.split(':')[1]))) >= 60:
            print(name)


