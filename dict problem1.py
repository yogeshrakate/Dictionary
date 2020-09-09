#WAPT update a dictionary with content of another dictionary
d1={'a':350,'b':200,'c':351}
d2={'b':400,'e':300,'f':250}
for i in d2:
    if i not in d1:
        d1[i]=d2[i]
    else:
        d1[i]=d1[i]+d2[i]
print(d1)
