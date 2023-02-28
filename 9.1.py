def func(a: int, b: int, c: str):
    if isinstance(a, int) and isinstance(b, int):
        return f'{a + b}{c}'
    return -1

try:
    print(func('wow', 'call', 911))
except Exception as error:
    print(error)
