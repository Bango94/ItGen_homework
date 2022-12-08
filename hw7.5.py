text = input()

text = text.split()
print(max(text,key=len))