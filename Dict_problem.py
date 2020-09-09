import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
ascend_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',ascend_d)
descend_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',descend_d)
