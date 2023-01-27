def convert(string):
    count_lower = len(list(filter(str.islower, string)))
    count_upper = len(list(filter(str.isupper, string)))
    if count_lower >= count_upper:
        return string.lower()
    return string.upper()


print(convert('pythON'))