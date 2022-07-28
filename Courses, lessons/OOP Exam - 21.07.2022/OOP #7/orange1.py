class Orange:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

    def __repr__(self):
        return f'sort {self.sort}, vitamins {self.vitamins}, price {self.price}, name {self.name}'