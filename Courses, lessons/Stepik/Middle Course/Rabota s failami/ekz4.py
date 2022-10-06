with open('words.txt', 'r', encoding='utf-8') as file:
    lst = file.read().split()
longest = len(max(lst, key=len))
print(*filter(lambda x: len(x) == longest, lst), sep='\n')