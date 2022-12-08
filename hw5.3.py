import math
x=float(input('x='))
y=float(input('y='))
R=4

hypotenusa=math.sqrt(x**2+y**2)

if hypotenusa<=R:
    print('point is within circle')
else:
    print('point is NOT within circle')