yr=int(input("year="))

if not yr % 4 and yr % 100 or not yr % 400:
    print("not usual year")
else:
    print("usual year")
