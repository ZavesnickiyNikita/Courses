#  4.	Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (массив из пяти элементов).
# Создать класс School:
# Добавить возможность для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)
class Students:

    def __init__(self, surname, name,patronymic, group, performance):
        self.surname = surname
        self.name = name
        self.group = group
        self.performance = performance

    def info(self):
        pass

    def score_5_or_6(self):
        if set(self.performance) == {5, 6}:
            print(f"Студент с оценками 5, 6 и его группа: {self.surname}, {self.group}")

    def print_number_of_group(self, group):
        if self.group == group:
            print(f"Студент {self.surname} в группе {self.group}")

    def average_performance_7(self, level):
        if (sum(self.performance) / len(self.performance)) >= level:
            print(f"Студент {self.surname} претендует на автомат. Средний балл больше или равен {level}")

class School:

    def __init__(self, students):
        self.students = students

    def get_list_of_students(self):     # Получить список студентов
        return self.students

    def admission(self, student):
        self.students.append(student)

student1 = students(('Ivanov', 'Ivan', 'Ivanovich', 1, [7, 8, 9, 6, 10, 7]))
student2 = students(('Petrov', 'Petr', 'Petrovich', 2, [5, 6, 8, 4, 6, 9]))
student3 = students(('Sidorov', 'Nikolai', 'Nikolaevich', 3, [6, 5, 5, 6, 6, 5]))
student4 = students(('Sviridov', 'Dmitriy', 'Dmitrievich', 4, [5, 3, 2, 5, 6, 2]))







