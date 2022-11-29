num = int(input())
ls_1, ls_2, result = [], [], []
for i in range(num):
    email = input()
    ls_1.append(email.split('@')[0])

num_2 = int(input())
for i in range(num_2):
    new_email = input()
    ls_2.append(new_email.split('@')[0])

for i in ls_2:
    name = ''
    count = 0
    if i in ls_1:
        name = i +  + '@beegeek.bzz'
        result.append(name)
    else:
        result.append(i + '@beegeek.bzz')



print(*result, sep='\n')
