
def razryadi():
    n = float(input())
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

print(razryadi())
