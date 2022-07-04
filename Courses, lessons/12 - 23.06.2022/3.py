import os

f = open('123.txt', 'w')    # Открытие файла в режиме записи
f.write('Hello World')        # Запись текста в файл
f.close()

# os.rename('123.txt', 'abc.txt')     # переименование файла

print('Текущая деректория: ', os.getcwd())

# os.mkdir('folder')                # Создание каталога

# os.chdir('folder')                  # Переход в каталог

print('Текущая директория изменилась на folder:', os.getcwd())

# os.chdir('..')                      # Вернуться в предыдущую папку

print('Сейчас директория такая: ', os.getcwd())

# os.makedirs('nested1/nested2/nested3')        # Создали папки nested1/nested2/nested3

print('Сейчас деректория такая', os.getcwd())

# os.remove('123.txt')            # Удалить файл

# os.rmdir('folder')              # удалить папку

# os.removedirs('nested1/nested2/nested3')    # удалить вложенные папки





