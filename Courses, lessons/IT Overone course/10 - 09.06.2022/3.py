# Создать произвольный словарь.
dictationary = {1: 2, 3: 4}

dictationary['five'] = 5  # Добавил ключ и значение
print(dictationary)

dictationary[(6,)] = [1, 2, 3, 4]  # Добавил ключ кортеж и значение список
print(dictationary)

print(dictationary[(6,)])   # Вывел значение по ключу

del dictationary[(6,)]     # Удалил значение по ключу
print(dictationary)

print(dictationary.keys())   # Вывел все ключи
