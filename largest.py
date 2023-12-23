'''a=[1,9,11,23,65,78,43]
out=a[0]
for var in a:
    if out<var:
        out=var
print(out)'''
 


'''a=[1,9,11,23,65,78,43]
out=a[0]
for var in a:
    if out>var:
        out=var
print(out)'''
a=[-1,-234,-4567,3445,67,98]
out=a[0]
out2=a[0]
for i in a:
    if out<i:#if out<var:
        out2=out
        out=i
    elif out2<i:#   for var in a:
        out2=i  #if out2<var and var!=out:
                #out2=var
print(out2)
