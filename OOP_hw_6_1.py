class Rectangle:

    def __init__(self, h: int, w: int):
        if h < 0 or w < 0:
            raise ValueError('Values cannot be less than 0')
        self.h = h
        self.w = w
        # self.n = n

    def area(self):
        return self.h * self.w

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return self.area() + other.area()

    def __mul__(self, other):
        return self.area() * other


a = Rectangle(2, 5)
b = Rectangle(3, 5)
print(a < b)
print(a+b)
print(a.__mul__(other=10))