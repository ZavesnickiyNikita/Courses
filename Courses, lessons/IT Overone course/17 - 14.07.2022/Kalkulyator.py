
class Calculator():


    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def umnojenie(self):
        return self.a * self.b

    def delenie(self):
        return self.a / self.b

    def vvod_znachenii(self):
        self.a = int(input('Введите первое число'))
        self.b = int(input('Введите второе число'))

while True:
    my_calculator = Calculator()
    my_calculator.vvod_znachenii()
    answer = input('Введите операцию')
    if answer == '+':
        print(my_calculator.plus())

    elif answer == '-':
        print(my_calculator.minus())

    elif answer == '*':
        print(my_calculator.umnojenie())

    elif answer == '/':
        print(my_calculator.delenie())





