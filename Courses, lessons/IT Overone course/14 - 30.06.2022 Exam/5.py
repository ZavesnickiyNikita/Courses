# 5.	Создайте словарь из строки ' An apple a day keeps the doctor away'    следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству
# вхождений данной буквы в строку.

w = 'An apple a day keeps the doctor away'
dictationary = {i: w.count(i) for i in w}
print(dictationary)