def is_valid(string):
    if len(string) in (4, 5, 6) and string.isdigit() and string.count(' ') == 0:
        return True
    else:
        return False


print(is_valid('8912'))


