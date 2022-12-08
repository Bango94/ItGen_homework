import random
a = [random.randint(1,20000) for i in range(3)]
b = sum(a) / len(a)
print(a)
print(b)