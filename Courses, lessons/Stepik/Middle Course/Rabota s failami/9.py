with open('population.txt', 'r', encoding='utf-8') as countries:
    for country in countries:
        n, p = country.split('\t')
        if n[0] == 'G' and int(p) >= 500_000:
            print(n)




