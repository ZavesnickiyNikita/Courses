from random import *

with open('first_names.txt', 'r', encoding='utf-8') as first_names, open('last_names.txt', 'r',
                                                                         encoding='utf-8') as last_names:
    imena, familii = [], []
    for first_name, last_name in zip(first_names.read().split(), last_names.read().split()):
        imena.append(first_name)
        familii.append(last_name)
    for i in range(3):
        print(choice(imena), choice(familii))
