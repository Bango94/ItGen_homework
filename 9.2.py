def func(n, m):
    return f"{'*' * m}\n" + \
        f"*{' ' * (m - 2)}*\n" * (n - 2) + \
        '*' * m
print(func(33,10))



