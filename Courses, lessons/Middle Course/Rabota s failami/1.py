import random

files = open('lines.txt', 'r', encoding='utf-8')

print(files.readlines()[random.randint(0, 2)])

files.close()