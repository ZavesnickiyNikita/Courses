with open('ledger.txt', 'r', encoding='utf-8') as file:
    summ = sum(map(lambda x: int(x[1:]), file.readlines()))
    print('$', summ, sep='')
