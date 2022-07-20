
class Example:
    default_1 = 14
    default_2 = 23

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_default(self):
        self.c = 5
        return self.c

    def find_summ(self):
        return self.default_1 + self.default_2

    def find_kvadrat(self):
        return self.a ** self.b

my_example = Example(4, 3)

print(my_example.print_default())
print(my_example.find_summ())
print(my_example.find_kvadrat())


