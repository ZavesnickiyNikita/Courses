import random

def generate_password():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    chars_1 = []
    ques_1 = input('Сколько паролей сгенерировать для Вас?')
    ques_2 = input('Какая длина пароля?')
    ques_3 = input('Должен ли пароль содержать цифры?')
    ques_4 = input('Должен ли пароль содержать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
    ques_5 = input('Должен ли пароль содержать строчные буквы abcdefghijklmnopqrstuvwxyz?')
    ques_6 = input('Должен ли пароль содержать символы !#$%&*+-=?@^_?')
    ques_7 = input('Исключать неоднозначные символы il1Lo0O ?')
    ques_1 = int(ques_1)
    if ques_3.lower() in 'даlfyes':
        chars += digits
    if ques_4.lower() in 'даlfyes':
        chars += uppercase_letters
    if ques_5.lower() in 'даlfyes':
        chars += lowercase_letters
    if ques_6.lower() in 'даlfyes':
        chars += punctuation
    for i in range(int(ques_1)):
        if ques_7 in 'даlfyes':
            for i in range(int(ques_2)):
                if chars.count(chars[i]) > 1:
                    while chars[i] == random.sample(chars):
                        chars.replace(i, random.sample(chars))
        print(*random.sample(chars, int(ques_2)), sep='')
    print('Вот ваши пароли, скопируйте их')

def choose_yes_no():
    while True:
        ans = input('Вам нужно сгенерировать парооль?')
        if ans.lower() in 'даlfyes':
            generate_password()
        elif ans.lower() in 'нетnoytn':
            print('Всего хорошего')
            break
        else:
            print('"Да" или "Нет?"')

choose_yes_no()
