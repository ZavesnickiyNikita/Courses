def hide_card(card):
    new_card = card.replace(' ', '')
    result = new_card.replace(new_card[:12], '*' * 12)
    return result



card = '3456 9012 5678 1234'

print(hide_card(card))