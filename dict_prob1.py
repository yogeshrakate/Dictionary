d={1:['a','b'],2:['c','d']}
l=[]
for i in d[1]:
    for j in d[2]:
        l.append(i+j)
print(l)