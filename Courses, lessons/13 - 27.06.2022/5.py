# 8.	Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

dict = {1: 2, 3: 4, 5: 6, 7: 8}
pr_keys = 1
pr_items = 1
for i in dict.keys():
    pr_keys *= i
for j in dict:
    pr_items *= dict[j]
print('Произведение ключей', pr_keys)
print('Произведение значений', pr_items)