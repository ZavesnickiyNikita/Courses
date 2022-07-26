class Robot:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def __repr__(self):
        return f'A robot {self.name} with {self.weapon} and {self.armor}'
