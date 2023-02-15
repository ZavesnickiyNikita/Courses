import string


ls_1, ls_2, result = [], [], []

num = int(input())
for i in range(num):
    email = input()
    ls_1.append(email.split('@')[0])


num_2 = int(input())
for i in range(num_2):
    new_email = input()
    ls_2.append(new_email.split('@')[0])


for i in ls_2:
    if i not in ls_1:
        result.append(f'{i}@beegeek.bzz')
    else:
        count = 0
        for j in ls_2:
            if j in ls_1:
                count += 1
        result.append(f'{j}{count}@beegeek.bzz')

print(result)




