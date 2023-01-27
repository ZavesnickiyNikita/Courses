
class Armor:

    def __init__(self, name, streigth, weight):
        self.name = name
        self.streigth = streigth
        self.weight = weight

    def __repr__(self):
        return f'{self.name} with streight {self.streigth} and weigth {self.weight}kg'