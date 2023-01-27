num = int(input())
last = num % 10
flag = True
while num != 0:
    last_digit = num % 10
    if last_digit < last:
        flag = False
    else:
        last = last_digit
    num = num // 10
if flag == True:
    print('YES')
else:
    print('NO')








