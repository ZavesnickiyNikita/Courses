def start():
    print('Start')


def stop():
    print('Stop')


def pause():
    print('Pause')


commands = {'start': start, 'stop': stop, 'pause': pause}  # словарь соответствия команда → функция

command = input()        # считываем название команды

commands[command]()