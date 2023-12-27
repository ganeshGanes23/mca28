'''a=[1,5,6,7,8,9,2]
count=0
i=0
while i<=len(a):
    
    count+=a[i]
    i+=1
print(count)'''

'''def rec2(a,i=0):
    if len(a)-1==i:
        return a[i]
    return a[i]+rec2(a,i+1)
out=rec2([1,5,6,7,8,9,2])
print(out)'''


def gana(x,i=0):
    if len(x)-1==i:
        if x[i]%2==0:
            return x[i]
        else:
            return x[i]
    if x[i]%2==0:
    
        return x[i]+gana(x,i+1)
    else:
        return gana(x,i+1)
out=gana([1,5,6,7,8,9,2])
print(out)



    

