import OOP_hw_5_2_module_student

class Group:
    def __init__(self, group_title: str, max_students = 10):
        self.group_title = group_title
        self.max_students = max_students
        self.students_list = []

    # adding_by_id
    def add_student(self, student: OOP_hw_5_2_module_student):
        if not isinstance(student, OOP_hw_5_2_module_student):
            raise TypeError('The student isn`t instance of class Student')
        if len(self.students_list) >= self.max_students:
            raise ValueError('The list of students cannot be extended as it is fully formed')
        else:
            for element in self.students_list:
                if student.id == element.id:
                    break
            self.students_list.append(student)

    #removal by id
    def removal_student(self, student: OOP_hw_5_2_module_student):
        for element in self.students_list:
            if student.id == element.id:
                self.students_list.remove(element)
