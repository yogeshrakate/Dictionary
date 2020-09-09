d={1:['a','b'],2:['c','d']}
l=[]
for i in range(len(d[i])):
    s=''
    for j in d:
        s+=d[j][i]
    l.append(s)
print(l)