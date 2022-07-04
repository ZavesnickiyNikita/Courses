
f = open('Example.txt', 'r')
# print(f.read(7))            # Выводит первые 7 символов файла
print(f.readline())           # Прочитает первую строку
print(f.readline())           # Прочитает вторую строку
print(f.readlines())
f.close()



