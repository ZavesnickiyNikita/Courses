import string 


old_mails, new_mails = {}, {}


for _ in range(int(input())):
    old_posts = input()
    for letter in old_posts:
        if any(map(str, letter)) in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            old_mails.setdefault(old_posts.split(string.digits)[0], old_posts.split(string.digits)[1])
        else:
            old_mails.setdefault(old_posts.split('@')[0], 0)


print(old_mails)


