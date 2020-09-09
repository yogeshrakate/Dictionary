
d={'id':[],'name':[],'age':[]}
l1=[]
l2=[]
l3=[]
n=int(input("Enter how many entries?:"))
for i in range(n):
    l1.append(i+1)
    l2.append(input("Enter name:"))
    l3.append(int(input("Enter age:")))
d['id']=l1
d['name']=l2
d['age']=l3
print(d)
'''
n=int(input("Enter how many entries?:"))
d={'id':[i+1 for i in range(n)],'name':[input("Enter Name: ") for i in range(n)],'age':[int(input("Enter age:")) for i in range(n)]}
print(d)
'''
