d={'id':[],'name':[],'age':[]}
n=int(input("Enter how many entries?:"))
for i in range(n):
    for k in d:
        if k=='id' or k=='age':
            d[k].append(int(input(f'Please enter {k}')))
        else:
            d[k].append(input(f'please enter {k}'))
print(d)
