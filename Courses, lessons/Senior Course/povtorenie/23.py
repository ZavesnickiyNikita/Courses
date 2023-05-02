
old_mails, new_mails = [], []
dct_mails = {}
for i in range(int(input())):
    old_mails.append(''.join(input().split('@')[0]))


for i in range(int(input())):
    new_mail = input()
    
    if new_mail in old_mails:
        print('yes')
    else:
        print('no')



      
