"""
1
"""


def geometric_progression(denominator: int, stop: int):


    start = 1

    while start * denominator <= stop:
        yield f"{start} * {denominator} = {start * denominator}"
        start += 1

    return


print("-" * 42)
print("geometric progression generator:")
for i in geometric_progression(7, 70):
    print(f"    {i}")

print("-" * 35)
# -------------------------------------------

"""
2
"""


def range_func(*args, **kwargs):


    if not args or len(args) > 3:
        raise TypeError

    start = args[0] if len(args) >= 2 else 0
    stop = args[1] if len(args) >= 2 else args[0]
    step = args[2] if len(args) == 3 else 1

    if not step:
        raise ValueError

    if start < 0 and stop > start:
        return

    if step > 0 and stop < start:
        return

    while start < stop:
        yield start
        start += step

    return


range1 = range_func(4, 20, 2)

print("analog to range():")
for i in range1:
    print(f"    {i}")

print("-" * 35)
# -------------------------------------------

"""
3
"""


def prime_numbers(multiplier_args):


    start = 2

    while start <= multiplier_args:
        prime_numbers_list = [1 for i in range(2, start + 1) if start % i == 0]

        if len(prime_numbers_list) > 1:
            start += 1
            continue

        else:
            yield start

        start += 1

    return


print("generator of simple numbers:")
for i in prime_numbers(25):
    print(f"    {i}")

print("-" * 35)
# -------------------------------------------

"""
4
"""


def numbers_list(entry_args):

    return (i ** 3 for i in range(2, entry_args))


print('generator of numbers raised into a cube:\n   ', *numbers_list(10))