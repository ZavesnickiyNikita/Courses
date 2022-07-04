a = float(input("введите число"))
b = float(input("введите второе число"))
oper = input("введите действие")
if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "*":
    print(a*b)
elif oper == "/":
    print(a/b)
elif oper == "//":
    print(a//b)
elif oper == "%":
    print(a%b)
else:
    print("неправильно ввели что-то")


