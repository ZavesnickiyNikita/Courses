
class Example():

    default_1 = 5
    default_2 = 6

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def print_d(self):
        self.d = 5
        print(self.d)

    def return_summ(self):
        return self.default_1 + self.default_2

    def vozvesti_v_stepenb(self):
        return self.number1 ** self.number2


my_exaple = Example(2, 3)

my_exaple.print_d()
print(my_exaple.vozvesti_v_stepenb())
print(my_exaple.return_summ())



