d={1:['a','b'],2:['c','d']}
l=[]
l1=(d.values())
for i in l1[0]:
    for j in l1[1:]:
        for k in j:
            l.append(i+k)
print(l)