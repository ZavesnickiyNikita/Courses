string = "1a2b3c4d"

dictionary = {letter: int(number) for number, letter in zip(string[::2], string[1::2])}
print(dictionary)

