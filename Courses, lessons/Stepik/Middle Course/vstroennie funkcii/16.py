abscissas = [input()]
ordinates = [input()]
applicates = [input()]

print(all(map(lambda x, y, z: True if x ** 2 + y ** 2 + z ** 2 >= 4 else False, zip(abscissas, ordinates, applicates) )))