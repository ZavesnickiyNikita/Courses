def create_phone_number(n):
    lst = []
    for i in n:
        lst.append(map(str, n))

    return f'({lst[0:3]}) {lst[3:6]}-{lst[6:]}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

