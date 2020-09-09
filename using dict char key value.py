#WAPT get even indexed character as key and odd indexed character as its value
s='the quick brown fox jumps over the lazy the brown dog'
l=list(s)
#print(l)
d={}
l1=[]
for i in range(0,len(l)-1,2):
    if l[i] not in d and l[i+1].isspace()==False:
        d[l[i]]=l[i+1]
    else:
        l1.append(l[i])
print(d)
print(l1)
