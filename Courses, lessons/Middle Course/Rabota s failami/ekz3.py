with open('grades.txt', 'r', encoding='utf-8') as file:
    count = 0
    for line in file.readlines():
        if all(map(lambda x: int(x) >= 65, line.split(' ')[1:])):
            count += 1
    print(count)