psw = input()

print("YES" if all([any(map(lambda x: x.isdigit(), psw)), any(map(lambda x: x.islower(), psw)),
                    any(map(lambda x: x.isupper(), psw)), len(psw) >= 7]) else "NO")

