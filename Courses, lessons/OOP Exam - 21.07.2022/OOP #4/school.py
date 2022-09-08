class School:

    def __init__(self, students):
        self.students = students

    def get_list_of_students(self):  # Получить список учеников
        return self.students

    def postupili_v_school(self, student):  # Кто поступил в школу
        self.students.append(student)

    def remove(self, student, group):  # Удаление по номеру группы
        if student.group == group:
            self.students.remove(student)

    def print_names(self):  # Вывести имена студентов
        list_names = []
        for student in self.students:
            list_names.append(student.name)
        return list_names

    def print_group(self, group):
        students = []  # Студенты по номеру группы
        for student in self.students:
            if student.group == group:
                students.append(student)
            return students

    def get_list_automat(self, auto_mark=7):  # Список на автомат, у кого оценки выше 7
        list_automate = []
        for student in self.students:
            average_mark = sum(student.score) / len(student.score)
            if average_mark >= auto_mark:
                list_automate.append(student)
        return list_automate

    def get_list_with_need_marks(self, grades):
        new_list_students = self.students.copy()  # Списко студентов с определенными оценками
        for student in self.students:
            for mark in student.score:
                if mark not in grades:
                    new_list_students.remove(student)
                    break
        return new_list_students
