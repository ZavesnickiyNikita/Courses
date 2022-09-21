def narcissistic(value):
    a, b = [], int()
    val1 = value
    while value != 0:
        a.append(value % 10)
        value = value // 10
    for i in a:
        b += i ** (len(a))
    if b == val1:
        return True
    else:
        return False



print(narcissistic(7))