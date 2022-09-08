def build_query_string(params):
    sorted(params.keys())
    sp, sp1 = [], []
    for i in params.items():
        sp.append(i)
    sp.sort()
    for i in sp:
        sp1.append(f'{i[0]}={i[1]}')
    return '&'.join(sp1)




    # sp1, sp2 = [], []
    # for i in params.items():
    #     sp1.append(i)
    # sp1.sort()
    # for i in sp1:
    #     return f'{sp1[0][0]}={sp1[0][1]}&{sp1[1][0]}={sp1[1][1]}'

print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))