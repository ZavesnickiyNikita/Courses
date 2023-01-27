arr = [1,7,19,10,12,14,19,16,19,17,19,19,19]
b = 19
for i in arr:
    if i == b:
        arr.remove(i)
print(arr)