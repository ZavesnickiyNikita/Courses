with open('lines.txt', 'r', encoding='utf-8') as file:
    lst, sort_lst = [], []
    for line in file.readlines():
        lst.append(line.rstrip())
    sort_lst = sorted(lst, key=len, reverse=True)
    total_lst = []
    first_line = sort_lst[0]
    for line in sort_lst:
        if len(line) == len(first_line):
            total_lst.append(line)
    print(*total_lst, sep='\n')



