food = ['макароны', 'рис', 'гречка', 'картофель']
a = input()
for i in food:
    if i == a :
        print('Я не ем', a)
        break
    print('Отлично, вкусные' + i)
else:
    print('Хорошо, что не было пельменей')
print('Ужин окончен')