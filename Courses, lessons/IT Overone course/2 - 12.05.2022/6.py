s = "шалаш"
s = s.split(" ")
print(s)
s = ''.join(s)
print(s)
if s == s[::-1]:
    print("палидром")
else:
    print("не палиндром")