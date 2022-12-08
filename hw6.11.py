n=int(input('n='))
if n % 2:
    res = []
    j = 0
    for i in range(n, 0, -2):
        res.append(f"{' ' * j}{'*' * i}")
        j += 1

    res += res[-2::-1]
    result = '\n'.join(res)
    print(result)
else:
    print("enter another number")