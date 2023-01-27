n, x, y, a, b = [int(i) for i in input().split()]

li = [i for i in range(n + 1)]
li = li[:x] + li[y:x-1:-1] + li[y+1:]
li= li[:a] + li[b:a-1:-1] + li[b+1:]
print(*li[1:])

