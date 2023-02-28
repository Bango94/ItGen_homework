text = input('text=')
result={}
for i in set(text):
    result[i] = text.count(i)
print(result)
    
