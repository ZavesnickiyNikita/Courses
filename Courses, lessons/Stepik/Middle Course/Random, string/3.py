from string import *
import random


def generate_password(lenght):
    password, random_password = [], ''
    letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
    digits1 = '23456789'
    lower_letters1 = 'qazwsxedcrfvtgbyhnujmikp'
    upper_letters1 = 'QAZWSXEDCRFVTGBYHNUJMKLP'
    password.append(random.choice(digits1))
    password.append(random.choice(lower_letters1))
    password.append(random.choice(upper_letters1))
    for i in range(lenght - 3):
        random_letter = random.choice(letter)
        password.append(random_letter)
    random_password = ''.join(password)
    return random_password


def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))


count = int(input())
lenght = int(input())
generate_passwords(count, lenght)










