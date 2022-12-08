import random
a = [random.randint(1,100) for i in range(4)]
b=a[:]+[item*item for item in a]

print(b)
