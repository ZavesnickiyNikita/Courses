

n = int(input())    # Кол-во чисел
count = 0
s = []
for i in range(n):
    i = int(input())    # Числа, которые проверяются
    s.append(i)
p = int(input())        # На это число проверяется произведение
if len(s) > 1:                  # на случай если кол-во чисел = 1, сразу "НЕТ"
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                if  s[i] * s[j] ==p:
                    count = 1
                    break
    if count == 1:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')






