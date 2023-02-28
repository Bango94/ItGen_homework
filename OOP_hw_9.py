"""
1
"""


def generation_func(first_member_of_progression, n_member):

    def count():
        nonlocal first_member_of_progression
        first_member_of_progression += first_member_of_progression
        return first_member_of_progression

    for i in range(n_member):
        yield first_member_of_progression
        first_member_of_progression = count()
    return


print("-" * 35)

for i in generation_func(1, 5):
    print(f"    {i}")
# -------------------------------------------

"""
2
"""

import time


def fibonacci():

    serial_numbers = {}
    first_number = 0
    second_number = 1

    def next_number(number):
        nonlocal first_number
        nonlocal second_number

        if number in serial_numbers:
            return serial_numbers[number]

        elif number == 0:
            serial_numbers[number] = 0

        elif number == 1:
            serial_numbers[number] = 1

        else:
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
            serial_numbers[number] = next_number

        return serial_numbers[number]

    return next_number


start = time.time()
fibo = fibonacci()

print("-" * 35)
for i in range(20):
    print(f"    {fibo(i)}")

print("-" * 35)
print("time ", time.time() - start)
# -------------------------------------------

"""
3
"""


def sum_list(list, func):

    return sum(func(number) for number in list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = lambda x: x / 2

print("-" * 35)
print("func:", sum_list(list, temp))