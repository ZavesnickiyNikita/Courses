
class Human():

    #  Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        #  Динамические поля
        #  Публичные
        self.name = name
        self.age = age
        #  Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def defail_info():
        print(f'Defail Name {Human.default_name}')
        print(f'Default Age {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

Human.defail_info()

alex = Human('Nikita', 26)
alex.info()

alex.earn_money(5000)
alex.earn_money(20000)
alex.info() 