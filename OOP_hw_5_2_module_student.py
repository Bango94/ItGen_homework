import OOP_hw_5_2_module_person

class Student(OOP_hw_5_2_module_person.Person):
    def __init__(self, name: str, surname: str, id: int, age: int):
        super().__init__(name, surname, id)
        self.age = age

    def __str__(self):
        return super().__str__() + f'{self.age} '
