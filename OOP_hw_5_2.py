import OOP_hw_5_2_module_student
import OOP_hw_5_2_module_group

student_01 = OOP_hw_5_2_module_student.Student('Ivan', 'Ivanov', 1, 21)
student_02 = OOP_hw_5_2_module_student.Student('Petr', 'Ivanov', 2, 22)
student_03 = OOP_hw_5_2_module_student.Student('Sergey', 'Ivanov', 3, 23)
student_04 = OOP_hw_5_2_module_student.Student('Pavel', 'Pavlov', 4, 24)
student_05 = OOP_hw_5_2_module_student.Student('Anton', 'Antonov', 5, 25)
student_06 = OOP_hw_5_2_module_student.Student('Yana', 'Yanovna', 6, 26)
student_07 = OOP_hw_5_2_module_student.Student('Svetlana', 'Svetlova', 7, 27)
student_08 = OOP_hw_5_2_module_student.Student('Yevgeniya', 'Yevgenova', 8, 28)
student_09 = OOP_hw_5_2_module_student.Student('Liubov', 'Liubimova', 9, 29)
student_10 = OOP_hw_5_2_module_student.Student('Liliya', 'Lilova', 10, 30)

group_Python = OOP_hw_5_2_module_group.Group('Python')
group_Python.add_student(student_01)
group_Python.add_student(student_02)
group_Python.add_student(student_03)
group_Python.add_student(student_04)
group_Python.add_student(student_05)
group_Python.add_student(student_06)
group_Python.add_student(student_07)
group_Python.add_student(student_08)
group_Python.add_student(student_09)

student_011 = OOP_hw_5_2_module_student.Student('Maksim', 'Ivanov', 11, 31)
student_001 = OOP_hw_5_2_module_student.Student('Ivan', 'Ivanov', 1, 21)

# group_Python.add_student(student_011)
group_Python.removal_student(student_001)
print (*group_Python.search_student('Ivanov'))

print (group_Python)