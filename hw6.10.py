for n in range (2,101):
    for i in range(2,n):
        if not n % 2:
            break
    else:
        print(n)