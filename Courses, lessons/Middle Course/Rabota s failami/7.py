with open('file.txt', 'r', encoding='utf-8') as file:
    letters, words, lines, lst = [], 0, 0, []
    for line in file.readlines():
        for i in line:
            if i.isalpha():
                letters.append(i)
        words += len(line.split())
        lst.append(line.split('\n'))
    print(f'Input file contains:\n{len(letters)} letters\n{words} words\n{len(lst)} lines')

