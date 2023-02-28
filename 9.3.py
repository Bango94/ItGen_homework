def search(seq, x):
    for index, item in enumerate(seq):
        if item == x:
            return index
    return -1

x= [5,7,13,24,12,15,5]
res= search(x,99)
if res:
    print(res)
else:
    print('error')


