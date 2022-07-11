#  Операции с файлами
import os

os.getcwd()

os.makedirs('New lesson')

os.chdir('New lesson')

os.getcwd()

a = open('test_1.txt', 'w')
b = open('test_2.txt', 'w')
c = open('test_3.txt', 'w')
a.close()
b.close()
c.close()
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')

os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')


os.chdir('..')
os.getcwd()
os.rmdir('New lesson')
