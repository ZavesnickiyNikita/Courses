
class Car:

    #  создание метода класса
    def __str__(self):
        return 'Car class object'

    def start(self):
        print('Двигатель заведен')

car_a = Car()
print(car_a)