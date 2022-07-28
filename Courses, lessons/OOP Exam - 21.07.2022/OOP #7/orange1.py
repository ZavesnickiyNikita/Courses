class Orange:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

    def __repr__(self):
        return f'Sort {self.sort}, vitamins {self.vitamins}, price {self.price}, name {self.name}'

    def clear(self):
        print(f'{self.name} is clear')