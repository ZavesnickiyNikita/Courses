
class Human:        # Human - Название класса
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, km):
        if km > 5:
            return f'Я не могу пройти {km} км'
        else:
            return f'Я могу пройти {km} км'


my_human = Human('Nikita', 26)  # my_human - экземпляр класса
km = int(input('Введите кол-во километров'))
print(my_human.walk(km))
print(my_human.name)
print(dir(my_human))
print(my_human.age)

class Car:

    #  Статические поля ( переменные класса)
    default_color = 'Grey'
    default_weight = 2450

    def __init__(self, color, model):
        #  Динамические поля
        self.color = color
        self.model = model

    def turn_on(self):
        pass

my_car = Car('blue', 'audi')
my_car.color = input('Введите цвет')
print(my_car.default_color)
print(my_car.default_weight)
print(my_car.color)
print(my_car.model)
