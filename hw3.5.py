x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
if z<x>y:
    print("x")
else:
    if z<y>x:
        print ("y")
    else:
        if y<z>x:
            print ("z")