with open(input(), 'r', encoding='utf-8') as file:
    for line in file.read().split('\n')[-10:]:
        print(line.rstrip())