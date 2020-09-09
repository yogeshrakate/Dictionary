'''d={1:['a','b'],2:['c','d']}
problem1 o/p==['ac','bd']
problem2 o/p==['ac','ad','bc','bd']'''

d={1:['a','b'],2:['c','d']}
"""l=[]
for i in range(len(d)):
    s=''
    for j in d:
        s+=d[j][i]
    l.append(s)
#print(l)
p=[]
r=[]
for k in d.keys():
    r.append(d[k])
print(r)
"""
def product(args):
    pools = list(args.values())
    print("pools: ",pools)
    result = [[]]
    for pool in pools:
        print("for pool", pool)
        result = [x+[y] for x in result for y in pool]
        print('result: ',result)
    d1=[]
    for prod in result:
        d1.append(''.join(prod))
    print(d1)
product(d)
def product(args, repeat=1):
    pools = list(args.values())
    print("pools: ",pools)
    result = [[]]
    for pool in pools:
        print("for pool", pool)
        
        for y in result:
            for x in result:
                result.append(x+[y])
        print('result: ',result)
    d1=[]
    for prod in result:
        d1.append(''.join(prod))
    print(d1)
product(d)












