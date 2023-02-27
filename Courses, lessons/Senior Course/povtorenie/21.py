import string as st


old_mails, ls = {}, []
for _ in range(int(input())):
    mail = input().split('@')[0]
    # if any(map(lambda x: x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'), mail)):
    if any(map(lambda x: x.isnumeric(), mail)):
        num = mail[-1]
        old_mails.setdefault(mail.rstrip(st.digits), num)
    else:
        old_mails.setdefault(mail.split('@')[0], 0)
        


# print(old_mails)


            




