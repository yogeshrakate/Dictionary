#WAPT get even indexed word as key and odd indexed word as its value
s='the quick brown fox jumps over the lazy the brown dog'
l=s.split()
d={}
l1=[]
for i in range(0,len(l)-1,2):
    if l[i] not in d:
        d[l[i]]=l[i+1]
    else:
        l1.append(l[i])
print(d)
print(l1)
