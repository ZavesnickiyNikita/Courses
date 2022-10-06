a = input()
with open(a, 'r', encoding='utf-8') as file:
    print(len(file.readlines()))