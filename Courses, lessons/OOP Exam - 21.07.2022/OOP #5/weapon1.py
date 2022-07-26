
class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def __repr__(self):
        return f'{self.name} have a damage {self.damage} and durability {self.durability}'