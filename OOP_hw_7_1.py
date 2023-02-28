class Person:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def __str__(self):
        return f'{self.name} {self.surname} {self.id} '

class Student(Person):
    def __init__(self, name: str, surname: str, id: int, age: int):
        super().__init__(name, surname, id)
        self.age = age

    def __str__(self):
        return super().__str__() + f'{self.age} '

class Group:
    def __init__(self, group_title: str, max_students = 10):
        self.group_title = group_title
        self.max_students = max_students
        self.students_list = []

    # adding_by_id
    def add_student(self, student: Student):
        if len(self.students_list) < self.max_students:
            for element in self.students_list:
                if student.id == element.id:
                    break
            self.students_list.append(student)

    #removal by id
    def removal_student(self, student: Student):
        for element in self.students_list:
            if student.id == element.id:
                self.students_list.remove(element)

    #searching by surname
    def search_student(self, surname: str) -> list:
        list_students_found = []
        for element in self.students_list:
            if element.surname == surname:
                list_students_found.append(element)
        return list_students_found

    def __getitem__(self, get_students):
        if isinstance(get_students, int):
            if 0 >= get_students > self.max_students:
                return IndexError
            return self.students_list[get_students]
        if isinstance(get_students, slice):
            result = []
            start = get_students.start or 0
            stop = get_students.stop or self.n + 1
            step = get_students.step or 1

            for get_student in range(start, stop, step):
                result.append(self.students_list[get_student])
            return result

        raise TypeError()

    # def __len__(self):
    #     return self.max_students

    def __str__(self):
        return f"\n{'Students list:'}\n{'-'*30}\n" + \
               f"{'Group:'} {self.group_title} \n{'-' * 30}\n" + \
               '\n'.join(map(str, self.students_list)) +'\n'

student_01 = Student('Ivan', 'Ivanov', 1, 21)
student_02 = Student('Petr', 'Ivanov', 2, 22)
student_03 = Student('Sergey', 'Ivanov', 3, 23)
student_04 = Student('Pavel', 'Pavlov', 4, 24)
student_05 = Student('Anton', 'Antonov', 5, 25)
student_06 = Student('Yana', 'Yanovna', 6, 26)
student_07 = Student('Svetlana', 'Svetlova', 7, 27)
student_08 = Student('Yevgeniya', 'Yevgenova', 8, 28)
student_09 = Student('Liubov', 'Liubimova', 9, 29)
student_10 = Student('Liliya', 'Lilova', 10, 30)

group_Python = Group('Python')
group_Python.add_student(student_01)
group_Python.add_student(student_02)
group_Python.add_student(student_03)
group_Python.add_student(student_04)
group_Python.add_student(student_05)
group_Python.add_student(student_06)
group_Python.add_student(student_07)
group_Python.add_student(student_08)
group_Python.add_student(student_09)

student_011 = Student('Maksim', 'Ivanov', 11, 31)
student_001 = Student('Ivan', 'Ivanov', 1, 21)

group_Python.add_student(student_011)
group_Python.removal_student(student_001)
print (*group_Python.search_student('Ivanov'))
print (group_Python)

print (group_Python[0])
print (group_Python[8])
print()
print ('\n'.join(map(str, group_Python[2:5])))
print()
