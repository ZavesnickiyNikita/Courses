#  калькулятор, если / на 0 то: "на ноль делить нелья", если
# левый символ, то неверная операция
a = int(input())
b = int(input())
oper = input()
if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "*":
    print(a*b)
elif oper == "/":
    if b != 0:
        print(a/b)
    else:
        print('На ноль делить нельзя!')
elif oper != "+" != "-" != "*" != "/":
    print('Неверная операция')





