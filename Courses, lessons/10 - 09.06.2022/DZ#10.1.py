#   С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
# В случае равенства вывести на экран все гласные буквы.
count_vowels = 0
count_consonants = 0
sp_vowels = []
for i in input():
    if i.lower() in 'ёяыуаеио':         # Рз упала на лапу азора   (Пример чтобы было равно кол-во)
        count_vowels += 1               # А роза упала на лапу азора (Пример не равно)
        sp_vowels.append(i.lower())
    elif i.lower() in 'йфцчвскмпнртгьшлбщдзжхъ':
        count_consonants += 1

print('Count of vowels:', count_vowels)
print('Count if consonants:', count_consonants)
if count_vowels == count_consonants:
    print('The same numbers of vowels and consonants. Output vowels:')
    print(*sp_vowels, sep = ', ')


