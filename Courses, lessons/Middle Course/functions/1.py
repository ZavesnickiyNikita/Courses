def matrix(row=None, string=None, value=None):
    if row is None:
        row = 1
    if string is None:
        string = row
    if value is None:
        value = 0
    mat = [[0] * string for i in range(row)]
    for i in range(row):
        for j in range(string):
            mat[i][j] = value
    return mat


print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))


