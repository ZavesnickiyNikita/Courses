with open('input.txt', 'r', encoding='utf-8') as input:
    a = input.readlines()

with open('output.txt', 'w', encoding='utf-8') as file:
    for index, strings in enumerate(a):
        file.write(f'{index + 1}) {strings}')

