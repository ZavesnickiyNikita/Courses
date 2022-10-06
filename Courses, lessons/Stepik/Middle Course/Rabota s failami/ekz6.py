lst_forbidden_words = []
str_file = str
with open('forbidden_words.txt', 'r', encoding='utf-8') as file, open('data.txt', 'r+', encoding='utf-8') as words:
    for word in file.read().split():
        lst_forbidden_words.append(word)

    str_file = words.read()

for i in str_file.split():
    if i.lower().rstrip() in lst_forbidden_words:
        str_file.replace(i, 'abc')
for i in str_file.split():
    if i == 'abc':
        print('*')
    else:
        print(i)




