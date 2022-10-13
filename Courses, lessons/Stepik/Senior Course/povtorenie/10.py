def choose_plural(amount, declensions):
    if str(amount)[-1] == '1':
        if str(amount)[-2:] == '11':
            return f'{amount} {declensions[2]}'
        else:
            return f'{amount} {declensions[0]}'
    if str(amount)[-1] in ['2', '3', '4']:
        if str(amount)[-2:] in ['12', '13', '14']:
            return f'{amount} {declensions[2]}'
        else:
            return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'



print(choose_plural(12, ('цент', 'цента', 'центов')))