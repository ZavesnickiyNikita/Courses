def find_amount():
    count_vowels, count_consonants = 0, 0
    for i in n:
        if i in 'qzwsxdcrfvtgbhnjmklp':
            count_consonants += 1
        elif i in 'aeyuio':
            count_vowels += 1
    print(f'Количество гласных {count_vowels}')
    print(f'Количество согласных {count_consonants}')
n = input()
find_amount()