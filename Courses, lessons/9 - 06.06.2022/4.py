person = {'name': 'Nikita', 'age': 26, 'city': 'Minsk'}
print(person)
print(person['age'])

person_1 = dict(name = 'Nikita', age = 26, city = 'Minsk')
print(person_1)
print(person['age'])

person_2 = dict(zip(['name', 'age', 'city'], ['Nikita', 26, 'Minsk' ]))
print(person_2)
print(person['age'])
