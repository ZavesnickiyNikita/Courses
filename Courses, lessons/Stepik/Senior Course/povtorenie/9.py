def spell(*args):
    return {i[0].lower():len(i) for i in sorted(args, key=len)}


words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']

print(spell(*words))








