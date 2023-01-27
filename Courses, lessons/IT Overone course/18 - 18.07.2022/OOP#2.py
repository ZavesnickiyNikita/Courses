
class Student:

    def __init__(self, name, money):
        self.name = name
        self.money = money

student_1 = Student('Petya', 120)
student_2 = Student('Kolya', 140)
student_3 = Student('Nikolay', 1000)

students = [student_1, student_2, student_3]
monyes = []

for i in students:
    monyes.append(i.money)
print(monyes)

if max(monyes) == min(monyes):
    print('all')
else:
    max_money = 0
    for i in students:
        if i.money > max_money:
            max_money = i.money
            name = i.name

print(max_money)
print(name)
