# Проверить, если ли в последовательности дубликаты

set1 = {1, 2, 3, 4, 5, 'nik', 'mike'}
set2 = {6, 7, 8, 9, 10, 'mike', 'nike'}
liste = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
set3 = set(liste)
if len(liste) == len(set3):  # Проверить есть ли дубликаты в списке
    print('True')
else:
    print('False')
liste1 = list(set3)
print(liste1)   # Список, у которого все дубликаты удалены
print(set1 & set2)
