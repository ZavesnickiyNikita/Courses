import random
from school import School
from student import Student

student_1 = Student('Иванов', 'Иван', 'Иванович', '10А', [random.randrange(4, 11) for i in range(10)])
student_2 = Student('Сидоров', 'Сергей', 'Сергеевич', '10А', [random.randrange(4, 11) for i in range(10)])
student_3 = Student('Петров', 'Петр', 'Петрович', '10Б', [random.randrange(7, 9) for i in range(10)])
student_4 = Student('Николаев', 'Николай', 'Николаевич', '10Б', [random.randrange(4, 11) for i in range(10)])
student_5 = Student('Никитин', 'Никита', 'Никитович', '10Б', [random.randrange(4, 11) for i in range(10)])

school_1 = School([])

school_1.postupili_v_school(student_1)
school_1.postupili_v_school(student_2)
school_1.postupili_v_school(student_3)
school_1.postupili_v_school(student_4)
school_1.postupili_v_school(student_5)

print(school_1.get_list_of_students())
print(school_1.get_list_automat())
print(school_1.get_list_with_need_marks([7, 8]))
print(school_1.print_names())
print(school_1.print_group('10А'))
