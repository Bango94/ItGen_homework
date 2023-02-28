row_1 = input ('row_1=')
row_2 = input ('row_2=')

res = {i for i in set(row_1) & set(row_2) if i.isalpha() }
print(res)
