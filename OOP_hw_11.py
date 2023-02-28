"""
1. Создайте дескриптор, который будет делать поля класса управляемые им доступными только для чтения.
"""
class ReadOnlyDescriptor:

    def __init__(self, x):
        self.x = x

    def __get__(self, *args, **kwargs):
        return self.x

    def __set__(self, *args, **kwargs):
        raise ValueError('Read only parameter')

    def __delete__(self, *args, **kwargs):
        raise ValueError('Read only parameter')


class AB:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    nice = ReadOnlyDescriptor('Nice!')


ab = AB(4, 5)
print(ab.nice)

""""
2. Реализуйте функционал, который будет запрещать установку полей класса любыми значениями,
# кроме целых чисел. Т.е., если тому или иному полю попытаться присвоить, например, строку,
# то должно быть возбужденно исключение.
"""

class Integer:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Only integer allowed.")
        self.__dict__[key] = value


ab1 = Integer(5, 6)
# ab1.nice = 'Nice!'
ab1.number = 6

""""
3. Реализуйте свойство класса, которое обладает следующим функционалом:
# при установки значения этого свойства в файл с заранее определенным названием
# должно сохранятся время (когда устанавливали значение свойства) и установленное значение.
"""
import datetime


class DateTimeValue:

    def __init__(self, a):
        self.a = a

    def __get__(self, b, classvalue):
        return self.a

    def __set__(self, b, value):
        with open('date_time_value.txt', 'a') as f:
            f.write(f'Value = {self.a}, Time: {datetime.datetime.now()}\n')
            self.a = value

    def __delete__(self, b):
        del self.a


class AB1:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    nice = DateTimeValue('Nice!')


ab2 = AB1(3, 5)
print(ab2.nice)
ab2.nice = 'Cool'
ab2.nice = 'Perfect'

"""
4.Реализуйте метакласс, который обладает следующим функционалом: при его использовании в файл с заранее
# определенным названием нужно сохранить имя класса и список его полей.
"""

class MetaMeta(type):

    def __new__(typeclass, class_name, supers, class_dict):
        return type.__new__(typeclass, class_name, supers, class_dict)

    def __init__(self, class_name, supers, class_dict):
        with open('Metaclass_file', 'w') as f:
            f.write(f'{class_name}:''\n')
            for i in class_dict:
                f.write(i)


class FromMeta(metaclass=MetaMeta):

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


a = FromMeta(1)
b = FromMeta(2)
print(a+b)

"""
5.Создайте ABC класс с абстрактным методом проверки целого числа на простоту.
# Т.е., если параметром этого метода является целое число и оно простое,
# то метод должен вернуть True, а в противном случае False.
"""
import abc


class Prime(abc.ABC):

    @abc.abstractmethod
    def prime_numbers(self):
        ...

"""
6. Создайте класс его наследующий.
"""
class Smth1(Prime):

    def __init__(self, n):
        self.n = n

    def prime_numbers(self):
        if not isinstance(self.n, int) or self.n <= 0:
            return False
        for i in range(2, self.n):
            if not self.n % i:
                return False

        return True

"""
7. Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом.
# Зарегистрируйте его в качестве виртуального подкласса.
"""

class Smth2:

    def __init__(self, n):
        self.n = n

    def prime_numbers(self):
        if not isinstance(self.n, int) or self.n <= 0:
            return False
        for i in range(2, self.n):
            if not self.n % i:
                return False

        return True


Prime.register(Smth2)

m = Smth2(7)

"""
8. Проверьте работоспособность проекта.　
"""
print(isinstance(m, Prime))
print(Smth1(5).prime_numbers())
print(Smth2(10).prime_numbers())

