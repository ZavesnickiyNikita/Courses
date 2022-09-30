
file = open('numbers.txt', 'r', encoding='utf-8')

print(sum(map(int, file)))

file.close()