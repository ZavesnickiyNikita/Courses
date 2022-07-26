class Student:

    def __init__(self, surname, name, patronomyc, group, score):
        self.surname = surname
        self.name = name
        self.patronomyc = patronomyc
        self.group = group
        self.score = score

    def __repr__(self):
        return self.name