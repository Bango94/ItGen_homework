a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
if a + b > c and a + c > b and c + b > a:
    print("Triangle exists")
else:
    print("Triangle not exists")