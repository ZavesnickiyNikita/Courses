# with open('E:/Никита/Python_for_professional/тест/2', 'r') as file:
#     print(*file)


def same_parity(numbers=[]):
    lst = []
    if numbers == []:
        return []
    if numbers[0] % 2 == 0:
        lst.append(list(filter(lambda x: x % 2 == 0, numbers)))
    if numbers[0] % 2 != 0:
        lst.append(list(filter(lambda x: x % 2 != 0, numbers)))
    for i in lst:
        return i


print(same_parity([]))
