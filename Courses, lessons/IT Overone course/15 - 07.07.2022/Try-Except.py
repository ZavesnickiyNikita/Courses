
a = int(input())
b = int(input())
try:
    total = a / b
except ZeroDivisionError:
    total = 'На ноль делить нельзя'
print(total)