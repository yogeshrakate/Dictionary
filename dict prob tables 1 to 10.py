#WAPT form a dict of tables of 1-10
'''d={}
for i in range(1,11):
    d[i]=[i*1,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10]
print(d)'''


#WAPT form a dict of tables of 1-10
d={}
for i in range(1,11):
    l=[]
    for j in range(1,11):
        l.append(i*j)
    d[i]=l
print(d)
