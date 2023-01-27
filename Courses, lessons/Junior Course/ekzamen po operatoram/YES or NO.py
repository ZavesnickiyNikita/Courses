number = int(input())
if number % 2 != 0:
    print('YES')
elif number % 2 ==0:
    if 2 <= number <= 5:
        print('NO')
    elif 6 <= number <= 20:
        print('YES')
    elif number > 20:
        print('NO')
