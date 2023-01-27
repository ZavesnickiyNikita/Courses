from orange1 import Orange

class Banana(Orange):
    def __init__(self, sort, vitamins, price, name, num_of_kalium):
        super().__init__(sort = sort, vitamins = vitamins, price = price, name = name)
        self.num_of_kalium = num_of_kalium

    def __repr__(self):
        return f'Sort {self.sort}, vitamins {self.vitamins}, price {self.price}, name {self.name}, kalium {self.num_of_kalium}'

