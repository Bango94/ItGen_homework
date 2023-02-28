"""
1
"""


class counter_decorator:


    def __init__(self, function):
        self.count = 0
        self.function = function

    def __call__(self, x, y, operator="+"):
        self.count += 1
        return self.function(x, y, operator)


@counter_decorator
def some_function(x, y, operator):


    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "**": lambda x, y: x ** y
    }

    action_operator = operators.get(operator)

    return f"{x} {operator} {y} = {action_operator(x, y)}"


print("-" * 77, "\n")

print(f"result: {some_function(10, 2)}\n\t"
      f"call {type(some_function)} №: {some_function.count}")

print("-" * 56)

print(f"result: {some_function(-3, 5, '-')}\n\t"
      f"call {type(some_function)} №: {some_function.count}")

print("-" * 56)

print(f"result: {some_function(20, 4, '*')}\n\t"
      f"call {type(some_function)} №: {some_function.count}")
# -------------------------------------------

"""
2
"""
function_list = []


def func_list_decorator(some_func):


    def wrapper():


        function_list.append(some_func)

        return function_list

    return wrapper


@func_list_decorator
def first_function():


    return "first func"


@func_list_decorator
def second_function(lst, multiplier):


    return [i * multiplier for i in lst]


some_list = [1, 2, 3, 4, 5]

print()
print("*" * 77)
print(f"Function registered as: {first_function()}")
print(f"now functions registered as: {second_function()}")

print()
print(f"list: {some_list}\n\t"
      f"now we have such list: {function_list[1](some_list, 3)}")
# -------------------------------------------

"""
3
"""


def save_to_file_decorator(func):


    def wrapper(*args, **kwargs):


        class_name_str = f"{func.__qualname__.split('.')[0]}.txt"
        res = func(*args, **kwargs)

        with open(class_name_str, encoding='utf-8', mode='w') as f:
            f.write(res)

        return res

    return wrapper


class Person:


    def __init__(self, surname, name, patronymic, birthdate):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate

    @save_to_file_decorator
    def __str__(self):
        return f"Saved: {self.surname} {self.name} {self.patronymic}. Date of birth: {self.birthdate}"


person = Person("Vasilovich", "Andrii", "Vals", "24.08.1975")

print()
print("*" * 77)
print(person)
# -------------------------------------------

"""
4
"""

import time


def set_time_and_write_to_file(number=1, file_name='script_work_time.txt'):
    i = 0
    start = time.time()

    while i < number:
        def func(func):
            def run_function(*args, **kwargs):
                res = func(*args, **kwargs)
                return res

            return run_function

        i += 1

        with open(file_name, encoding='utf-8', mode='w') as file:
            work_time = time.time() - start
            file.write(f"on {i} iterations, took {work_time} seconds")

    return func


@set_time_and_write_to_file(50)
def fibonacci(k):
    if k == 0:
        return 0
    return 1 if k in [1, 2] else fibonacci(k - 1) + fibonacci(k - 2)


find_fibo_number = 20

print()
print("*" * 77)
print(f"{find_fibo_number}-number - {fibonacci(find_fibo_number)}")